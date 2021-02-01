#!/usr/bin/python3

from jnpr.junos import Device
from lxml import etree
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.scp import SCP
from pprint import pprint
from datetime import datetime
import re

today = datetime.now().strftime("%d-%h-%Y")
username = "ysaied"

Leafs = {
  "Leaf1" : "192.0.0.61",
  "Leaf2" : "192.0.0.62",
  "Leaf3" : "192.0.0.63",
  "Leaf4" : "192.0.0.64",
  "Leaf5" : "192.0.0.65",
  "Leaf6" : "192.0.0.66",
  }

for leaf,oob in Leafs.items():
  dev = Device(host=oob, user=username, gather_facts="false")
  dev.open()
  config = dev.rpc.get_config()
  dev.close()
  #etree.dump(config)
  interfaces = config.findall('interfaces/interface')

  interface_list = list()
  for interface in interfaces:
    ifd = interface.find('name').text
    if re.search('^([xg]e|ae[3-9].*)', ifd):
      interface_list.append(ifd)

  file_name = "/var/tmp/" + leaf + "_sp-to-ent-migration_" + today + ".txt"
  #Open local file to load the configuration
  open_file = open(file_name, "w")

  uni_ifd=set()
  uni_vlan=set()
  for interface in interface_list:
    ifd = "interfaces/interface[name='"+interface+"']/unit"
    ifd_unit = config.findall(ifd)
    for unit in ifd_unit:
      if ((unit.find("name").text) != str(0)):
        vid = unit.find("vlan-id").text
        uid = unit.find("name").text
        uni_ifd.add(interface)
        uni_vlan.add(vid)
        print("delete interfaces {} unit {}".format(interface,uid), file=open_file)
        print("set interfaces {}.0 family ethernet-switching vlan members {}".format(interface,vid), file=open_file)
        print("delete vlans VLAN-{} interface {}.{}".format(vid,interface,uid), file=open_file)
    
  for interface in uni_ifd:
    print("set interfaces {}.0 family ethernet-switching interface-mode trunk".format(interface), file=open_file)
    print("set interfaces {}.0 family ethernet-switching storm-control storm-control-standard".format(interface), file=open_file)
  
  uni_vlan_list=list(uni_vlan)
  uni_vlan_list.sort()
  for vlan in uni_vlan_list:
    print("set vlans VLAN-{} vlan-id {}".format(vlan,vlan), file=open_file) 
  
  #Open local file to load the configuration
  open_file.close()
  
  with SCP(dev, progress=True) as scp:
    scp.put(file_name, remote_path="/var/home/"+username)
