from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
from jnpr.junos.op.ospf import OspfNeighborTable
from time import sleep

USER = "lab"
PASSWD = "lab123"
HOSTS = ["vmx-1", "vmx-2"]

def load_ospf_config(host):
    with open("ospf-{}.yaml".format(host)) as f:
        vars = yaml.load(f)
    with Device(host=host, user=USER, passwd=PASSWD) as dev:
        with Config(dev, mode="exclusive") as conf:
            conf.load(template_path="ospf.j2", template_vars=vars, format="text")
            conf.pdiff()
            if conf.diff() is not None:
                conf.commit()

def get_full_neighbor_count(host):
    count = 0
    with Device(host=host, user=USER, passwd=PASSWD) as dev:
        ospf_table = OspfNeighborTable(dev).get()
        for neighbor in ospf_table:
            if neighbor.ospf_neighbor_state == "Full":
                count += 1
    return count

if __name__ == "__main__":
    for host in HOSTS:
        print("Loading configuration on {}; the diff is:".format(host))
        load_ospf_config(host)

    ok_hosts = set()
    for _ in range(20):
        print("Waiting for OSPF to come up...")
        sleep(5)
        for host in HOSTS:
            if host not in ok_hosts:
                if get_full_neighbor_count(host) == 2:
                    ok_hosts.add(host)
        if len(ok_hosts) == len(HOSTS):
            print("Success!")
            break
    else:
        print("Something went wrong, please check.")
