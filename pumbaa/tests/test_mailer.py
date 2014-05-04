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

    def test_valid_email_init_message(self):
        sender = "hello@gmail.com"
        recipient = sender
        subject = sender

        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        msg = mailer._init_message(sender,recipient,subject,subject)
        regex = "From:.\w+@\w+.\w{2,}\\r\\nSubject:(.*?)\\r\\nTo:.\w+@\w+.\w{2,}\\r\\nMIME-Version:.1.0\\r\\nContent-Type:.text/html"
        self.assertRegex(msg.as_string(),regex)

    def test_invalid_sender_init_message(self):
        sender = "fadffaa"
        recipient = "hello@gmail.com"
        subject = "wow"
        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        self.assertRaises(Exception,mailer._init_message,sender,recipient,subject,subject)
    
    def test_invalid_recipient_init_message(self):
        recipient = "hgmail.com"
        sender = "hello@gmail.com"
        subject = "wow"
        from pumbaa.libs.mailer import Mailer
        mailer = Mailer()
        self.assertRaises(Exception,mailer._init_message,sender,recipient,subject,subject)
