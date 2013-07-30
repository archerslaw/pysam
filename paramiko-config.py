#!/usr/bin/python
#coding=utf-8

import os
import paramiko
from ConfigParser import ConfigParser

username='root'
password='redhat'
ConfigFile='config.ini'
config=ConfigParser()
config.read(ConfigFile)
hostname1=''.join(config.get('IP','ipaddress'))
address=hostname1.split(';')
print address

if __name__=='__main__':
    for ip in address:
        paramiko.util.log_to_file('paramiko.log')
        s=paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=ip, username=username, password=password)
        stdin,stdout,stderr=s.exec_command('ifconfig; free; df -h')
        print stdout.read()
        s.close()
