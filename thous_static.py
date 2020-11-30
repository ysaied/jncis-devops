#! /usr/bin/python

a = 0

#file_output = open("/var/tmp/test", "w")
#while a <= 255 :
#    b = 0
#    while b <= 255 :
#        print >> file_output,("set routing-options static route 192.1.{}.{}/32 reject".format(a,b))
#        b += 1
#    a += 1
#file_output.close()

config = """
set routing-instances l3vpn-{0} instance-type vrf"
set routing-instances l3vpn-{0} route-distinguisher 192.1.0.0:{1}"
set routing-instances l3vpn-{0} vrf-target target:192.1.0.0:{1}
"""

file_output = open("/var/tmp/l3vpn", "w")
while a <= 8000 :
    print >> file_output,(config.format("%04d"%a,a))
    a +=1
file_output.close()