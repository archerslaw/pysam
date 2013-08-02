#!/usr/bin/python
#coding:utf-8

import paramiko
import os
import datetime
from ConfigParser import ConfigParser
              
ConfigFile='config-mutiupload.ini'
config=ConfigParser()
config.read(ConfigFile)
hostname1=''.join(config.get('IP','ipaddress'))
address=hostname1.split(';')
print address

username='root'
password='redhat'
port=22
local_dir='/tmp/local/'
remote_dir='/tmp/remote/'

if __name__=="__main__":
    for ip in address:
        t=paramiko.Transport((ip, port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        #files=sftp.listdir(remote_dir)
        files=os.listdir(local_dir)
        for f in files:
            print ''
            print '####################################################'
            print 'Beginning to upload file to %s host.' % ip
            print datetime.datetime.now()
            print 'Uploading file: ',os.path.join(local_dir,f)
            #sftp.get(os.path.join(remote_dir,f), os.path.join(local_dir,f))
            sftp.put(os.path.join(local_dir,f), os.path.join(remote_dir,f))
            print 'Upload success %s.' % datetime.datetime.now()
            print ''
        t.close()
