#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import hashlib

def walk(path):
    isdir, isfile, join = os.path.isdir, os.path.isfile, os.path.join
    if not os.path.exists(path):
        print "%s: No such file or directory" % path
    else:
        lsdir = os.listdir(path)
        dirs = [i for i in lsdir if isdir(join(path,i))]
        files = [i for i in lsdir if isfile(join(path,i))]
        yield(path, dirs, files)
        if dirs:
            for d in dirs:
                for (p, d, f) in walk(join(path,d)):
                    yield (p, d, f)
        #yield(path, dirs, files)

def md5sum(f):
    md5 = hashlib.md5()
    fd = open(f)                                                                                                
    while True:
        data = fd.read(1024*4)
        if data:
            md5.update(data)
        else:
            break
    fd.close()
    return md5.hexdigest()
def issame(a, b):
    if md5sum(a) == md5sum(b):
        print '%s is the same file' % os.path.join(path, a)

def main():
    all_md5=[]
    for path, dirs, files in walk(sys.argv[1]):
        for f in files:
            pf = os.path.join(path,f)
            filemd5 = md5sum(pf)
            if filemd5 in all_md5:
                print "This file has same md5: %s" % pf
            else:
                all_md5.append(filemd5)

if __name__ == "__main__":
    main()

