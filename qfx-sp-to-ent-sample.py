#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.scp import SCP
from lxml import etree
from datetime import datetime
import re

today = datetime.now().strftime("%d-%h-%Y")
username = "juniper"

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
  vlans = config.findall('vlans/vlan')

  vlan_list = list()
  for vlan in vlans:
    vlan_name = vlan.find('name').text
    vlan_list.append(vlan_name)
  vlan_list.sort()

  file_name = "/var/tmp/{}_sp-to-ent-migration_{}.txt".format(leaf,today)
  open_file = open(file_name, "w")

  ifd_set=set()
  vlan_id_set=set()
  for vlan in vlan_list:
    ifl_xpath = "vlans/vlan[name='{}']/interface".format(vlan)
    ifl_list = config.findall(ifl_xpath)
    for ifl in ifl_list:
      ifl_name = ifl.find("name").text
      ifd_name = ifl_name.split(".")[0]
      ifd_set.add(ifd_name)
      vlan_id = vlan.split("-")[1]
      vlan_id_set.add(vlan_id)
      print("delete vlans {} interface {}".format(vlan,ifl_name), file=open_file)
      print("delete interfaces {}".format(ifl_name), file=open_file)
      print("set interfaces {}.0 family ethernet-switching vlan members {}".format(ifd_name,vlan_id), file=open_file)
  
  vlan_id_list=list(vlan_id_set)
  vlan_id_list.sort()
  for vlan_id in vlan_id_list:
    print("set vlans VLAN-{0} vlan-id {0}".format(vlan_id), file=open_file) 

  ifd_list=list(ifd_set)
  ifd_list.sort()  
  for ifd in ifd_list:
    print("set interfaces {}.0 family ethernet-switching interface-mode trunk".format(ifd), file=open_file)
    print("set interfaces {}.0 family ethernet-switching storm-control storm-control-standard".format(ifd), file=open_file)
  
  open_file.close()
  
  with SCP(dev, progress=True) as scp:
    scp.put(file_name, remote_path="/var/home/"+username)
