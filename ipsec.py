from jinja2 import Environment, FileSystemLoader

env = Environment(load=FileSystemLoader("jinja2"))
ipsec_jinja2 = env.get_template("ipsec.j2")

with open("vars/ipsec.yml") as file:
    data = load(file)

print (ipsec_jinja2.render(data))