#!/usr/bin/python
#coding:utf-8

import paramiko
import os
import datetime

hostname='192.168.3.121'
username='root'
password='redhat'
port=22
local_dir='/tmp/local/'
remote_dir='/tmp/remote/'

if __name__=="__main__":
    try:
        t=paramiko.Transport((hostname, port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        #files=sftp.listdir(remote_dir)
        files=os.listdir(local_dir)
        for f in files:
            print ''
            print '####################################################'
            print 'Beginning to upload file %s.' % datetime.datetime.now()
            print 'Uploading file:',os.path.join(local_dir,f)
            #sftp.get(os.path.join(remote_dir,f), os.path.join(local_dir,f))
            sftp.put(os.path.join(local_dir,f), os.path.join(remote_dir,f))
            print 'Upload file success %s.' % datetime.datetime.now()
            print ''
    except Exception:
        print "Error! Please check it."
        t.close()
