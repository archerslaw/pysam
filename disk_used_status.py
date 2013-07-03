#!/usr/bin/python
# -*- coding: utf-8 -*-

#磁盘利用率

import os

def disk_stat():
    hd={}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail/(1024*1024*1024)
    hd['capacity'] = disk.f_bsize * disk.f_blocks/(1024*1024*1024)
    hd['used'] = disk.f_bsize * disk.f_bfree/(1024*1024*1024)
    return hd

print disk_stat()
