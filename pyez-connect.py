#! /usr/bin/python

from jnpr.junos import Device


out_fname = "pyez_connect-" + datetime.now().strftime("%d%h%Y") + ".txt"
with open("./j2-results/" + out_fname, "w") as results:
    with Device(host="192.0.0.41", user="ysaied") as jnpr_node:
        print >> results, (jnpr_node.facts)
