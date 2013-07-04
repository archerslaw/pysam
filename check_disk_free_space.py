#!/usr/bin/python 
# -*- coding: utf-8 -*- 
########################################################## 
# @This script is used to check disk free space
# @Name:         check_disk_free_space.py 
# @Function:     check disk free space
"""主要用于zabbix监控系统硬盘只用，适用于windows和linux系统，返回值为0为正常，
有几个分区的硬盘剩余少于10G或低于10%就为报警阀值(windows的C盘和linux的根分区除外)"""
##########################################################

import platform 
import commands 
 
def w_disk(): 
    import wmi 
    c = wmi.WMI () 
    i = 0 
    for disk in c.Win32_LogicalDisk (DriveType=3): 
        a = int(disk.FreeSpace) / (1024*1024*1024) 
        b = int(100.0 * long (disk.FreeSpace) / long (disk.Size)) 
        if disk.Caption == "C:": 
            if (a < 2) or (b < 10): 
                i += 1 
            else: 
                i += 0 
        else: 
            if (a < 10) or (b < 10): 
                i += 1 
            else: 
                i += 0 
    print i 
 
def L_disk(): 
    free = commands.getstatusoutput('df -h|grep dev|egrep -v "tmp|var|shm"') 
    list = free[1].split('\n') 
    i = 0 
    for disk in range(len(list)): 
        vd = list[disk][6:8] 
        a = list[disk].split()[3] 
        if a[-1] == 'T': 
            a = int(float(a[:-1]))*1024 
        else: 
            a = int(float(a[:-1])) 
        b = 100 - int(list[disk].split()[4][:-1]) 
        if vd == "da": 
            if (a < 2) or (b < 10): 
                i += 1 
            else: 
                i += 0 
        else: 
            if (a < 10) or (b < 10): 
                i += 1 
            else: 
                i += 0 
    print i 
 
if __name__ == "__main__": 
    os = platform.system() 
    if os == "Windows": 
        w_disk() 
    elif os == "Linux": 
        L_disk()
