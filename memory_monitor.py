#!/usr/bin/python
#coding=utf-8

#内存利用率

import time
import sys

STATS = []

def Memory():
    mem = {}
    lines = open('/proc/meminfo').readlines()
    for line in lines:
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var)
    STATS[0:] = [mem['MemTotal']]
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    STATS[1:] = [mem['MemUsed']]
    u = round((mem['MemUsed'])/(mem['MemTotal']),5)
    STATS.append('%.2f%%'%(u*100))

if __name__ == '__main__':
    try:
        print 'Memory_Total      Memory_Used        Used_Per' 
        while True:
            time.sleep(1)
            Memory()
            MemT = STATS[0]
            MemU = STATS[1]
            Used_Per = STATS[2]
            print MemT ,'KB     ',MemU ,'KB       ',Used_Per  
    except KeyboardInterrupt, e:
        print "\nmemmonit exited"

