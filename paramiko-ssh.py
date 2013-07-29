#!/usr/bin/python
#coding=utf-8

import paramiko

hostname='10.66.9.242'
username='root'
password='redhat'

if __name__=='__main__':
    paramiko.util.log_to_file('paramiko.log')
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    #s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname,username=username,password=password)
    stdin,stdout,stderr=s.exec_command('ifconfig;free;df')
    print stdout.read()
    s.close()
