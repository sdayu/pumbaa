import unittest

class TestMailer(unittest.TestCase):
    
    def test_init_seesion(self):
        from pumbaa.libs.mailer import Mailer
        import smtplib
        mailer = Mailer()
        session = mailer._init_session()
        self.assertIsInstance(session,smtplib.SMTP)
        if isinstance(session,smtplib.SMTP):
            session.quit()

    def test_valid_email_init_header(self):
        sender = "hello@gmail.com"
        recipient = sender
        subject = sender

        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        headers = mailer._init_headers(sender,subject,recipient)
        regex = "From:.\w+@\w+.\w{2,}\\r\\nSubject:(.*?)\\r\\nTo:.\w+@\w+.\w{2,}\\r\\nMIME-Version:.1.0\\r\\nContent-Type:.text/html"
        self.assertRegex(headers,regex)

    def test_invalid_sender_init_header(self):
        sender = "fadffaa"
        recipient = "hello@gmail.com"
        subject = "wow"
        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        self.assertRaises(Exception,sender,subject,recipient)
    
    def test_invalid_recipient_init_header(self):
        recipient = "hgmail.com"
        sender = "hello@gmail.com"
        subject = "wow"
        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        self.assertRaises(Exception,sender,subject,recipient)
