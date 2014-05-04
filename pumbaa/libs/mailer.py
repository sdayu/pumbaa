import smtplib
import re
import configparser
from email.mime.text import MIMEText
from pyramid.threadlocal import get_current_registry

class Mailer():
    _regex_mail = "\w{2,}@\w{2,}.\w{2,}"

    def __init__(self):
        settings = get_current_registry().settings
        if settings is None:
           cfg = configparser.ConfigParser()
           cfg.read('../../development.ini')
           settings = dict(cfg.items('app:main'))

        self.set_mailer_enable(settings.get("mail.post_fb.enable",False))
        if self.enable:
            self.set_server(settings.get("mail.host"))
            self.set_port(settings.get("mail.port"))
            self.set_user(settings.get("mail.username",""),
            settings.get("mail.password",""))
            self.set_recipient(settings.get("mail.fb_group",""))
            self.set_forum_id(settings.get("mail.forum_id",[]))
             
    def post_to_fb_group(self,text):
        self.send_mail(self.recipient,None,text)
    
    def send_mail(self,recipient,subject,text):
        msg = self._init_message(self.sender,recipient,subject,text)
        try:
            session = self._init_session() 
            session.sendmail(self.sender, recipient, msg.as_string())
            session.quit()
        except smtplib.SMTPException:
            raise Exception('Error: unable to send email')

    def _init_session(self):
        session = smtplib.SMTP(self.server, self.port)

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.sender, self.password)
         
        return session

    def _init_message(self,sender,recipient,subject,text):

        if not re.search(self._regex_mail, sender):
            raise Exception('%s not valid email',sender)
        if not re.search(self._regex_mail,recipient):
            raise Exception('%s not valid email',recipient)

        msg = MIMEText(text.encode('utf-8'), 'plain', 'UTF-8')
         
        msg['From'] = sender
        msg['To'] = recipient
        if subject is not None:
            msg['Subject'] = subject.encode('utf-8')
        msg.set_charset('utf-8')

        return msg 
    
    def set_server(self,server):
        self.server = server

    def set_port(self,port):
        self.port = port

    def set_user(self,username,password):
        self.sender = username 
        self.password = password

    def set_recipient(self,recipient):
        self.recipient = recipient

    def set_mailer_enable(self,enable):
        if enable == "true" or enable == "True":
            self.enable = True
        else:
            self.enable = False

    def set_forum_id(self,forum_id):
        self.forum_id = forum_id.split()
