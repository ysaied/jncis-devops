from jnpr.junos import Device
import jcs

BASE_OID = '.1.3.6.1.4.1.2636.13.61.100.100'
SCRIPT_XPATH = {
    1: "system/scripts/op/file",
    2: "system/scripts/commit/file",
    3: "event-options/event-script/file",
    4: "system/scripts/snmp/file"
}

def main():
    snmp_action = jcs.get_snmp_action()
    snmp_oid = jcs.get_snmp_oid()
    jcs.syslog("8", "snmp_action = ", snmp_action, " snmp_oid = ", snmp_oid)
    if snmp_action != 'get':
        return
    if not snmp_oid.startswith(BASE_OID):
        return
    index = int(snmp_oid[len(BASE_OID)+1:])
    if index not in SCRIPT_XPATH:
        return
    with Device() as dev:
        conf = dev.rpc.get_config()
    count_scripts = len(conf.xpath(SCRIPT_XPATH[index]))
    jcs.emit_snmp_attributes(snmp_oid, "Integer32", str(count_scripts))

if __name__ == '__main__':
    main()
