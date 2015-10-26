#!/usr/bin/python
# script to connect to many IPv6 addresses
# requirements:
# pip install py2-ipaddress

import errno, ipaddress, socket, sys, time

remoteaddr = ipaddress.ip_address("fd::1")
remoteport = 5000
conns = 1500000

mylist = []

for i in range(conns):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.setblocking(0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.connect((str(remoteaddr), remoteport))
    except socket.error as e:
        if e.errno == errno.EINPROGRESS:
            pass
        else:
            raise
    mylist.append(s)
    remoteaddr += 1

print "Socket opens attempted: {0}".format(conns)
print "Press Ctrl+c to close sockets and end client"

while True:
   time.sleep(1)
