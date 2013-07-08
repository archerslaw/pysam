#!/usr/bin/python                                                                                                         
#coding=utf-8

from subprocess import Popen, PIPE

def getCpu():
    cmd = "cat /proc/cpuinfo"
    p = Popen(cmd, stdout = PIPE, stderr = PIPE, shell = True)
    stdout, stderr = p.communicate()
    return stdout
 
def parserCpu(stdout):
    groups = [i for i in stdout.split('\n\n')]
    #print groups
    group = groups[-2]
    cpu_list = [ i for i in group.split('\n')]
    cpu_info = {}
    for x in cpu_list:
        k, v = [i.strip() for i in x.split(':')]
        cpu_info[k] = v
    return cpu_info

if __name__ == "__main__":
    cpuinfo = parserCpu(getCpu())
    print cpuinfo
    print "------------------------------"
    print 'Processor number: %d' % (int(cpuinfo['processor']) + 1)
    print 'Vendor          : %s' % cpuinfo['vendor_id']
