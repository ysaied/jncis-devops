#!/usr/bin/python3

from jnpr.junos import Device
from lxml import etree
from jnpr.junos.utils.config import Config
from pprint import pprint
import re

Leafs = {
  "Leaf1" : "192.0.0.61",
  "Leaf2" : "192.0.0.62",
  "Leaf3" : "192.0.0.63",
  "Leaf4" : "192.0.0.64",
  "Leaf5" : "192.0.0.65",
  "Leaf6" : "192.0.0.66",
  }

for leaf,oob in Leafs.items():
  dev = Device(host=oob, user="ysaied", gather_facts="false")
  dev.open()
  config = dev.rpc.get_config()
  dev.close()

  #etree.dump(config)
  #print(etree.tostring(config, encoding='unicode', pretty_print=True))

  interfaces = config.findall('interfaces/interface')
  #print(etree.tostring(interfaces, encoding='unicode', pretty_print=True))

  interface_list = list()
  for interface in interfaces:
    ifd = interface.find('name').text
    if re.search('^[axg]e', ifd):
      interface_list.append(ifd)


  for interface in interface_list:
    ifd = "interfaces/interface[name='"+interface+"']/unit"
    ifd_unit = config.findall(ifd)
    for unit in ifd_unit:
      if ((unit.find("name").text) != str(0)):
        print("\n###unit {} with vlan-id {} found on interface {}".format(unit.find("name").text, unit.find("vlan-id").text, interface))
        print("delete interfaces {} unit {}".format(interface,unit.find("name").text))
        print("set interfaces {}.0 family ethernet-switching vlan members {}".format(interface,unit.find("vlan-id").text))
        print("delete vlans vlan-{} interface {}.{}".format(unit.find("vlan-id").text,interface,unit.find("name").text))
  #print(interface, unit)
