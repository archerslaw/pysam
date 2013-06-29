#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys
import os

#print sys.argv


def opt():
    parser = OptionParser(usage="usage: %prog [options] [file1 file2 ...]")
    parser.add_option("-c", "--char", 
                      dest="characters", 
                      action="store_true",
                      default=False,
                      help="Only count characters")
    parser.add_option("-w", "--words", 
                      dest="words", 
                      action="store_true",
                      default=False,
                      help="Only count words")
    parser.add_option("-l", "--lines", 
                      dest="lines", 
                      action="store_true",
                      default=False,
                      help="Only count lines")
    parser.add_option("-n", "--no-total", 
                      dest="nototal", 
                      action="store_true",
                      default=False,
                      help="print total or not")
    return parser.parse_args()
    #(options, args) = parser.parse_args()
    #return (options, args)
#print options,args



def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return (chars, words, lines)


def print_wc(chars, words, lines, fn):
    if options.characters:
        print chars,
    if options.words:
        print words,
    if options.lines:
        print lines,
    print fn

def main():
    if args: 
        t_lines, t_words, t_chars = 0, 0, 0
        for fn in args:
            if not os.path.exists(fn):
                print >>sys.stderr, "%s: No such file or directory" % fn
                #sys.stderr.write("%s: No such file or directory\n" %fn)
                continue
            if os.path.isdir(fn):
                sys.stderr.write("%s: Is a directory\n" %fn)
                continue
            if os.path.isfile(fn):
                f = open(fn)
                data = f.read()
                chars, words, lines = get_count(data)
                t_lines += lines
                t_words += words
                t_chars += chars
                print_wc(lines, words, chars, fn)
            else:
                print >> sys.stderr, "%s: No such file or directory" % fn
        if not options.nototal and len(args) > 1:
            print_wc(t_lines, t_words, t_chars, 'total')
    else:
        fn = "stdin"
        if path.exists(f):
            print '%s: %s: No such file or directory' % (wc-lwc-mutil-no-directory.py, f)
        else:
            data = sys.stdin.read()
            chars, words, lines = get_count(data)
            print_wc(chars, words, lines, fn)

if __name__ == "__main__":
    #global options, args
    (options, args) = opt()
    if not (options.characters or options.words or options.lines):
        options.characters, options.words, options.lines = True, True, True
    main()
