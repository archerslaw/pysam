#!/usr/bin/python
#coding:utf-8

import paramiko
import os
import datetime
from ConfigParser import ConfigParser
              
ConfigFile='config-nopasswdSSH.ini'
config=ConfigParser()
config.read(ConfigFile)
hostname1=''.join(config.get('IP','ipaddress'))
address=hostname1.split(';')
print address

username='root'
port=22
pkey='/root/.ssh/id_rsa'

if __name__=="__main__":
    key=paramiko.RSAKey.from_private_key_file(pkey)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    for ip in address:
        client.connect(hostname=ip, port=port, username=username, pkey=key)
        stdin,stdout,stderr = client.exec_command('ifconfig; free; df -h')
        print stdout.read()
        print '###########################################################'
        print ''
    client.close()
