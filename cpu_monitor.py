#!/usr/bin/python
#coding=utf-8

#cpu利用率

import time
import sys

TATS = []

def cpuinfo():
    lines = open('/proc/stat').readlines()
    for line in lines:
        ln = line.split()
        if ln[0].startswith('cpu'):
            return ln;
    return []
W = cpuinfo()
one_cpuTotal=long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])
one_cpuused=long(W[1])+long(W[2])+long(W[3])

if __name__ == '__main__':
    try:
        print 'CPU_per' 
        while True:
            time.sleep(2)
            W = cpuinfo()
            two_cpuTotal=long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])
            two_cpuused=long(W[1])+long(W[2])+long(W[3])
            cpuused=float(two_cpuused-one_cpuused)/(two_cpuTotal-one_cpuTotal)
            print '%.2f%%'%(cpuused*100)
    except KeyboardInterrupt, e:
        print "\ncpumonit exited"
