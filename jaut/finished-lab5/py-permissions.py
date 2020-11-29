from junos import Junos_Configuration as root
import jcs

if __name__ == "__main__":
    message = "Permission all is assigned to invalid class."
    for element in root.findall("system/login/class[permissions='all']"):
        jcs.emit_warning("class:" + element.findtext('name') + " " + message)

