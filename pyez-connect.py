#! /usr/bin/python

from jnpr.junos import Device

with Device(host="192.0.0.41", user="ysaied") as jnpr_node:
    print(jnpr_node.facts)