from jnpr.jsnapy import SnapAdmin
from pprint import pprint

config_data = """
hosts:
  - device: 172.25.11.1
    username : lab
    passwd: lab123
tests:
  - test_interfaces_up.yml
"""

js = SnapAdmin()
snapchk = js.snapcheck(config_data, "pre")
for val in snapchk:
    print "Tested on", val.device
    print "Final result: ", val.result
    print "Total passed: ", val.no_passed
    print "Total failed:", val.no_failed
    # pprint(dict(val.test_details))


