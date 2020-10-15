#! /usr/bin/python
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader("jinja2"))
ipsec_jinja2 = env.get_template("ipsec.j2")

with open("./vars/ipsec.yml", "r") as vars_yaml:
    ipsec_vars = yaml.load(vars_yaml, Loader=yaml.FullLoader)
    vars_yaml.close()

#print (data)
#print (ipsec_jinja2.render(ipsec_vars))

with open("./j2-results/junos.txt", "w") as config:
    print >> config, (ipsec_jinja2.render(ipsec_vars))
    config.close()
