class AutoPostFacebook():
    def __init__(self, request):
        from pyramid.threadlocal import get_current_registry
        settings = get_current_registry().settings

        from pyramid_mailer import get_mailer
        self.pymailer = get_mailer(request)

        self.set_mailer_enable(settings.get("mail.post_fb.enable", False))
        if self.enable:
            self.set_user(settings.get("mail.username", ""),
                          settings.get("mail.password", ""))
            self.set_recipient(settings.get("mail.fb_group", ""))
            self.set_forum_id(settings.get("mail.forum_id", []))

    def post_to_fb_group(self, text):
        from pyramid_mailer.message import Message

        message = Message(subject=None,
                          sender=self.sender,
                          recipients=[self.recipient],
                          body=text)

        self.pymailer.send_immediately(message, fail_silently=False)

    def set_user(self, username, password):
        self.sender = username
        self.password = password

    def set_recipient(self, recipient):
        self.recipient = recipient

    def set_mailer_enable(self, enable):
        if enable == "true" or enable == "True":
            self.enable = True
        else:
            self.enable = False

    def set_forum_id(self, forum_id):
        self.forum_id = forum_id.split()
