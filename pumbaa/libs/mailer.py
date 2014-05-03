import smtplib
import re
import configparser

class Mailer():
    _regex_mail = "\w{2,}@\w{2,}.\w{2,}"

    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read('../../development.ini')
        settings = dict(cfg.items('app:main'))

        self.set_server(settings["mail.host"])
        self.set_port(settings["mail.port"])
        self.set_user(settings["mail.username"],settings["mail.password"])
        self.set_recipient(settings["mail.fb_group"])
         
    def post_to_fb_group(self,body):
        self.send_mail(self.recipient,"ffs",body)
    
    def send_mail(self,recipient,subject,body):
        body = "" + body + ""
        headers = self._init_headers(self.sender,subject,recipient)
        try:
            session = self._init_session() 
            session.sendmail(self.sender, recipient, headers + "\r\n\r\n" + body)
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

    def _init_headers(self,sender,subject,recipient):

        if not re.search(self._regex_mail, sender):
            raise Exception('%s not valid email',sender)
        if not re.search(self._regex_mail,recipient):
            raise Exception('%s not valid email',recipient)

        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        return headers
    
    def set_server(self,server):
        self.server = server

    def set_port(self,port):
        self.port = port

    def set_user(self,username,password):
        self.sender = username 
        self.password = password

    def set_recipient(self,recipient):
        self.recipient = recipient
