from junos import Junos_Configuration as root
import jcs

if __name__ == "__main__":
    for unit in root.xpath("interfaces/interface/unit[apply-macro[name='FAMILIES']]"):
        unit_name = unit.findtext("name")
        interface_name = unit.findtext("../name")
        conf = """<interfaces>
                    <interface>
                    <name>{0}</name>
                      <unit>
                        <name>{1}</name>
                        <family>
                          <mpls/>
                          <iso/>
                        </family>
                      </unit>
                    </interface>
                  </interfaces>""".format(interface_name, unit_name)
        jcs.emit_change(conf, "transient-change", "xml")
