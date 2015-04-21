# -*- coding: utf-8 -*-
class Email(object):

    def __init__(self, to="", subject="", body="", attachment="", file_name=""):
        self.to = to
        self.subject = subject
        self.body = body
        self.attachment = attachment
        self.file_name = file_name

    @classmethod
    def random(cls):
        from random import randint
        return cls(to="saga9119+" + str(randint(0, 1000000)) + "@gmail.com",
                   subject="Subject text" + str(randint(0, 1000000)),
                   body="Body text " + str(randint(0, 1000000)))















