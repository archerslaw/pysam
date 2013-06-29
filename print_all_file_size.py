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

def main():
    for path, dirs, files in walk(sys.argv[1]):
        for f in files:
            print os.path.getsize(os.path.join(path,f)),
            print os.path.join(path,f)

if __name__ == "__main__":
    main()

