#!/usr/bin/python
#coding=utf-8
 
import paramiko

hostname='10.66.9.242'
username='root'
password='redhat'
port=22
localpath='/tmp/a.log'
filepath='/tmp/b.log'

if __name__=="__main__":
    sshport=paramiko.Transport((hostname, port))
    sshport.connect(username=username,password=password)
    sftptest=paramiko.SFTPClient.from_transport(sshport)
    sftptest.put(localpath,filepath)
    sftptest.close()
    sshport.close()
