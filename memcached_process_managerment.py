#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import Popen, PIPE

work_dir = "/var/tmp"

class Process(object):
    '''docstring for Process.'''
    def __init__(self, name,
                    program,
                    args,
                    work_dir
                ):
        #super(Process, self).__init__()
        self.name = name
        self.program = program
        self.args = args
        self.work_dir = work_dir

    def init(self):
        if not os.path.exists(self.work_dir):
            os.mkdir(self.work_dir)
        os.chdir(self.work_dir)

    def _pid_file(self):
        """
        /var/tmp/memeched/memcached.pid
        """
        return os.path.join(self.work_dir, '%s.pid' % self.name)
    
    def _write_pid(self):
        if self.pid:
            with open(self._pid_file(),'w') as fd:
                fd.write(str(self.pid))
    
    def _get_pid(self):
        if os.path.exists(self._pid_file()):
            with open(self._pid_file(),'r') as fd:
                self.pid = int(fd.read())
                return self.pid
        else:
            return None

    def isRunning(self):
        proc_pid = os.path.join('/proc','%s' % self._get_pid())
        return os.path.exists(proc_pid)

    def help(self):
        pass

    def start(self):
        self.init()
        command = '%s %s' % (self.program, self.args)
        p = Popen(command,shell=True)
        self.pid = p.pid
        self._write_pid()

    def stop(self):
        pid = self._get_pid()
        if self.isRunning():
            import signal
            os.kill(self.pid, signal.SIGTERM) # kill -15 xxx
            os.remove(self._pid_file())
        else:
            print "Stop it sccessfully."
    
    def status(self):
        pid = self._get_pid()
        """
        if pid:
            if self.isRunning():
                print 'It\'s running now...'
            else:
                print 'Not running!'
        else:
            print 'Pid file does not existing now.'
        """
        if self.isRunning():
            print 'It\'s running now...'
        else:
            print 'It isn\'t running.'

    def restart(self):
        self.stop()
        self.start()

def main():
    name = 'memcached'
    program = '/usr/bin/memcached'
    args = '-u nobody -p 11211 -m 64 -c 1024'
    wd = '/var/tmp/memcached'
    memp = Process(
            name = name,
            program = program,
            args = args,
            work_dir = wd
            )
    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print "Options error."
        sys.exit()
    cmds = ('start', 'top', 'restart', 'status')
    if cmd not in cmds:
        memp.help()
    if cmd == 'start':
        memp.start()
    elif cmd == 'stop':
        memp.stop()
    elif cmd == 'status':
        memp.status()
    elif cmd == 'restart':
        memp.restart()

if __name__ == "__main__":
    main()
