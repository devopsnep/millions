#!/usr/bin/python
# script to add many IPv6 addresses to an interface
# requirements:
# pip install py2-ipaddress
# pip install pyroute2

import errno, ipaddress, pyroute2, sys

remoteaddr = ipaddress.ip_address("fd::1")
conns = 1500000

ip = pyroute2.IPRoute()
index = ip.link_lookup(ifname='eth1')[0]

for i in range(conns):
    remoteaddr += 1
    try:
        ip.addr('add', index, address=str(remoteaddr), mask=96)
    except pyroute2.netlink.exceptions.NetlinkError as e:
        if e.code == errno.EEXIST:
            pass
        else:
            raise
    if (i%10000 == 0):
        print "added {0} addresses".format(i)

ip.close()
