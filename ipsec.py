#! /usr/bin/python
from jinja2 import Environment, FileSystemLoader
import yaml
from datetime import datetime

# Locate the Jinja2 directory
env = Environment(loader=FileSystemLoader("jinja2"))
# Load Jinja2 template
ipsec_jinja2 = env.get_template("ipsec.j2")

# open file to read the YAML 
with open("./vars/ipsec.yml", "r") as vars_yaml:
    ipsec_vars = yaml.load(vars_yaml, Loader=yaml.FullLoader)

# open file to write Jinja2 render results
out_fname = "ipsec-" + datetime.now().strftime("%d%h%Y") + ".txt"
print (out_fname)
with open("./j2-results/" + out_fname, "w") as config:
    print >> config, (ipsec_jinja2.render(ipsec_vars))
