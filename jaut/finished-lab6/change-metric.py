from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import argparse

arguments = {
    "area": "OSPF area number",
    "interface": "Name of the logical interface to change metric",
    "metric": "New metric value"
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for key in arguments:
        parser.add_argument('-' + key, required=True, help=arguments[key])
    args = parser.parse_args()

    metric_conf = "set protocols ospf area {0} interface {1} metric {2}".format(
        args.area, args.interface, args.metric)

    with Device() as dev:
        with Config(dev, mode="exclusive") as conf:
            conf.load(metric_conf)
            conf.commit()
