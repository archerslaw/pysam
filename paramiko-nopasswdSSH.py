#!/usr/bin/python

import paramiko

hostname='10.66.11.229'
port=22
username='root'
key='/root/.ssh/id_rsa'
mykey=paramiko.RSAKey.from_private_key_file(key)
s=paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname=hostname, port=port, username=username, pkey=mykey)
stdin,stdout,stderr=s.exec_command('ifconfig')
print stdout.read()
s.close()
