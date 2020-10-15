from jinja2 import Enviroment, FileSystemLoad

env = Enviroment(load=FileSystemLoad("jinja2"))
ipsec_jinja2 = env.get_template("ipsec.j2")

with open("vars/ipsec.yml") as file:
    data = load(file)

print (ipsec_jinja2.render(data))