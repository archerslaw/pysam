#!/usr/bin/python
#coding=utf-8

from subprocess import Popen, PIPE
import re

def getIfconfig():
    p = Popen('ifconfig', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout

def parserIfconfig(stdout):
    groups = [i for i in stdout.split('\n\n') if i and not i.startswith('lo')]
    #groups = [i for i in stdout.split('\n\n')]
    #print groups
    ifname = re.compile(r'^(wlan[\d])')       #(r'^(eth\d:?\d?)')
    macaddr = re.compile(r'.*HWaddr\s+([0-9a-fA-F:]{17})')
    ipaddr = re.compile(r'.*inet addr:+([\d.]{7,15})')
    result = []
    #print groups
    for group in groups:
        config_list = {}
        for line in group.split('\n'):
            #print line
            m_ifname = ifname.match(line)
            m_macaddr = macaddr.match(line)
            m_ipaddr = ipaddr.match(line)
            if m_ifname:
                config_list['ifname'] = m_ifname.group(1)
                #print config_list['ifname']
            if m_macaddr:
                config_list['macaddr'] = m_macaddr.groups()[0]
                #print config_list['macaddr']
            if m_ipaddr:
                config_list['ipaddr'] = m_ipaddr.groups()[0]
                #print config_list['ipaddr']
        result.append(config_list)
        """
        if not config_list:
            print config_list
        """
    return result

if __name__ == "__main__":
    output = getIfconfig()
    list = parserIfconfig(output)
    print 'All the ifname, ipaddr and macaddr info:'
    print list
    for x in list:
        #print x
        if 'ifname' in x:
            print 'The right ifname, ipaddr and macaddr info:'
            print x

