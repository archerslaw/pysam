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

def main():
    dir_md5 = open('directory_md5.txt', 'w')
    for path, dirs, files in walk(sys.argv[1]):
        for f in files:
            pf = os.path.join(path,f)
            dir_md5.write(pf)
            dir_md5.write(md5sum(pf))
    dir_md5.close()
    direct_md5_file = '/home/python_study/Python_Application/day2/directory_md5.txt' 
    len_file = len(open(direct_md5_file).read())
    if 0 !=len_file:
        print 'The md5 for the directory %s: ' % sys.argv[1] + md5sum(direct_md5_file)

if __name__ == "__main__":
    main()

