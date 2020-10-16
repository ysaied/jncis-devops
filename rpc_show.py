#! /usr/bin/python

from jnpr.junos import Device
from datetime import datetime
from lxml import etree

# output file name
out_fname = "rpc_show-" + datetime.now().strftime("%d%h%Y") + ".txt"

# open file to write 
with open("./j2-results/" + out_fname, "w") as results:
# create Device instance to connect and get device info
    with Device(host="192.0.0.41", user="ysaied") as jnpr_node:
        result_1 = etree.tostring(jnpr_node.rpc.get_system_uptime_information(), encoding='unicode', pretty_print=True)
        result_2 =  result_1.findtext("system-uptime-information/current-time/date-time")
        print >> results, (result_2)
