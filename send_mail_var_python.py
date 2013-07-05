#!/usr/bin/python 
# -*- coding: utf-8 -*- 
#导入smtplib和MIMEText 

import smtplib,sys 
from email.mime.text import MIMEText 
 
def send_mail(sub,content): 
    ############# 
    #要发给谁，这里发给1个人 
    mailto_list=["biao060798@163.com"] 
    ##################### 
    #设置服务器，用户名、口令以及邮箱的后缀 
    mail_host="smtp.163.com" 
    #smtp.163.com|pop.163.com
    mail_user="biao060798@163.com" 
    mail_pass="060798" 
    mail_postfix="163.com" 
    ###################### 
    ''' 
    to_list:发给谁 
    sub:主题 
    content:内容 
    send_mail("biao060798@163.com","sub","content") 
    ''' 
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">" 
    msg = MIMEText(content,_charset='gbk') 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = ";".join(mailto_list) 
    try: 
        s = smtplib.SMTP() 
        s.connect(mail_host) 
        s.login(mail_user,mail_pass) 
        s.sendmail(me, mailto_list, msg.as_string()) 
        s.close() 
        return True 
    except Exception, e: 
        print str(e) 
        return False 
if __name__ == '__main__': 
    if send_mail(u'<python测试邮件标题>',u'这是python发送的测试邮件的内容，谢谢。'): 
        print u'邮件发送成功，请登入您的邮箱，注意查收！' 
    else: 
        print u'发送失败, 请检查无误后再发！' 

