#!/usr/bin/python
# -*- coding: utf-8 -*-

#网卡流量监控

import time
import sys

if len(sys.argv) > 1:
    INTERFACE = sys.argv[1]
else:
    INTERFACE = 'wlan0'
STATS = []
print 'Interface:',INTERFACE

def rx():
    ifstat = open('/proc/net/dev').readlines()
    for interface in  ifstat:
        if INTERFACE in interface:
            stat = float(interface.split(":")[1].split()[0])
            STATS[0:] = [stat]

def tx():
    ifstat = open('/proc/net/dev').readlines()
    for interface in  ifstat:
        if INTERFACE in interface:
            stat = float(interface.split()[9])
            STATS[1:] = [stat]

if __name__ == '__main__':
    try:
        print 'In       Out'
        rx()
        tx()
        while True:
            time.sleep(1)
            rxstat_o = list(STATS)
            rx()
            tx()
            RX = float(STATS[0])
            RX_O = rxstat_o[0]
            TX = float(STATS[1])
            TX_O = rxstat_o[1]
            RX_RATE = round((RX - RX_O)/1024,3)
            TX_RATE = round((TX - TX_O)/1024,3)
            print RX_RATE ,'KB  ',TX_RATE ,'KB'

    except KeyboardInterrupt, e:
        print "\npyifstat exited"
