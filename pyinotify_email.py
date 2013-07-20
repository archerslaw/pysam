#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
使用脚本监视某目录下的文件增、删、改等操作，并将其结果发送Email到指定邮箱，本文只监视了文件被创建的事件。
"""

import os
import sys
import smtplib
import pyinotify
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
 
reload(sys)
sys.setdefaultencoding('utf8')
 
def send_Mail(full_filename):
    smtp = smtplib.SMTP()
    try:
        smtp.connect('smtp.163.com')
        smtp.login('biao060798@163.com', '060798')
    except smtplib.SMTPConnectError, error:
        print error
        sys.exit(2)
    # 构造MIMEMultipart对象做为根容器
    msg = MIMEMultipart()
    msg['From'] = u'biao060798@163.com'
    msg['To'] = u'biao060798@163.com'
    msg['Subject'] = u'测试邮件标题'
    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    msg.attach(MIMEText(os.path.basename(full_filename), 'plain', 'utf-8'))
    # 构造MIMEImage对象做为文件附件内容并附加到根容器
    ctype, encoding = mimetypes.guess_type(full_filename)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    # 读入文件内容并格式化
    try:
        data = open(full_filename, 'rb')
        file_msg = MIMEImage(data.read(), subtype)
    except IOError, error:
        print error
    ## 设置附件头
    basename = os.path.basename(full_filename)
    file_msg.add_header('Content-Disposition', 'attachment;filename="%s"' % basename)
    msg.attach(file_msg)
    smtp.sendmail(msg["From"], msg["To"], msg.as_string().encode('utf-8'))
    smtp.close()

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        # 取事件文件全路径
        self.full_name = os.path.join(event.path, event.name)
        # 取事件文件后缀名
        self.ext = os.path.splitext(self.full_name)[1]
        # 当匹配到PDF文件时，发送邮件
        if self.ext == '.pdf':
            send_Mail(self.full_name)
 
def main():
    # 被监视的目录
    path = '/tmp'
    wm = pyinotify.WatchManager()
    notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
    # 设置受监视的事件，这里只监视文件创建事件，（rec=True, auto_add=True）为递归处理
    wm.add_watch(path, pyinotify.IN_CREATE, rec=True, auto_add=True)
    notifier.start()
  
if __name__ == '__main__':
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, 'fork failed: %d (%s)' % (e.errno, e.strerror)
        sys.exit(1)
    os.chdir('/tmp')
    # 设置程序以daemon方式运行，不依赖于终端
    os.setsid()
    os.umask(0)
    main()
