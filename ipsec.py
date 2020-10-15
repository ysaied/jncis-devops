#! /usr/bin/python
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader("jinja2"))
ipsec_jinja2 = env.get_template("ipsec.j2")

with open("./vars/ipsec.yml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

#print (data)
#print (ipsec_jinja2.render(data))

with open("./j2-results/junos.txt", "w") as config:
    print >> config, (ipsec_jinja2.render(data))
    config.close()
