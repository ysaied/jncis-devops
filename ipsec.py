#! /usr/bin/python
from jinja2 import Environment, FileSystemLoader
from yaml import load

env = Environment(loader=FileSystemLoader("jinja2"))
ipsec_jinja2 = env.get_template("ipsec.j2")

with open("vars/ipsec.yml") as f:
    data = load(f)

print (ipsec_jinja2.render(data))