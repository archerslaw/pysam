#!/usr/bin/python
#coding=utf-8

'''
通过subprocess读取dmidecode内容,
System Information: Manufacturer, Product Name, Version, Serial Number, Family
'''
from subprocess import Popen, PIPE

def getDMI():
    p = Popen('dmidecode', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout

def parserDMI(dmidata):
    pd = {}
    line_in = False
    for line in dmidata.split("\n"):
        if line.startswith('System Information'):
            line_in = True
            continue
        if line.startswith('\t') and line_in:
            #print line
            k, v = [i.strip() for i in line.split(':')]
            pd[k] = v
        else:
            line_in = False
    return pd

if __name__ == "__main__":
    dmidata = getDMI() 
    #print dmidata
    print parserDMI(dmidata)
    print '-----------------------------'
    print 'Manufacturer : ' + parserDMI(dmidata)['Manufacturer']
    print 'Product Name : ' + parserDMI(dmidata)['Product Name']
    print 'Version      : ' + parserDMI(dmidata)['Version']
    print 'Serial Number: ' + parserDMI(dmidata)['Serial Number']
    print 'Family       : ' + parserDMI(dmidata)['Family']
