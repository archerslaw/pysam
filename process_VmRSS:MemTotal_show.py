#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def Split_Num(num):
    cmd = "cat /proc/%s/status | grep VmRSS" % num
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    data = p.communicate()[0]
    mem_proc = data.split()[1]
    return mem_proc

def Get_App_Mem(app_server):
    app_mem = 0
    cmd = "ps aux | grep %s | grep -v grep" % app_server
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    data = p.communicate()[0].split('\n')[:-2]
    for x in data:
        num = int(x.split()[1])
        app_mem += int(Split_Num(num))
    return app_mem

def MemTotal():
    cmd = "grep MemTotal /proc/meminfo"
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    data = p.communicate()[0]
    mem_total = data.split()[1]
    return mem_total

def Get_Proportion(app_server):
    if 0 == Get_App_Mem(app_server):
        return 'The %s Total VmRSS: 0' % app_server
    else:
        app_mem = float(Get_App_Mem(app_server))
        memtotal = int(MemTotal())
        return app_mem/memtotal

if __name__ == "__main__":
    print 'Httpd Total VmRSS: %s' % Get_App_Mem('httpd')
    print 'MemTotal of Host : %s' % MemTotal()
    print 'VmRSS / MemTotal : %s' % Get_Proportion('httpd')

