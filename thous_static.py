#! /usr/bin/python

a = 0

while a <= 255 :
    b = 0
    while b <= 255 :
        print ("set routing-options static route 192.1.{}.{}/32 reject".format(a,b))
        b += 1
    a += 1
