#! /usr/bin/python

from jnpr.junos import Device
from datetime import datetime

# output file name
out_fname = "pyez_connect-" + datetime.now().strftime("%d%h%Y") + ".txt"

# open file to write 
with open("./j2-results/" + out_fname, "w") as results:
# create Device instance to connect and get device info
    with Device(host="192.0.0.41", user="ysaied") as jnpr_node:
        print >> results, (jnpr_node.rpc.get_system_uptime_information)
