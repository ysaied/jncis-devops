from jnpr.junos import Device

if __name__ == "__main__":
    with Device() as dev:
        inv = dev.rpc.get_chassis_inventory()
        model = inv.findtext("chassis/description")
        sn = inv.findtext("chassis/serial-number")
        print "Model: " + model
        print "Serial Number: " + sn
        for module in inv.findall("chassis/chassis-module/name"):
            print "Chassis module: " + module.text
