# -*- coding: utf-8 -*-
class User(object):

    def __init__(self, email_login="", password="", email=""):
        self.email_login = email_login
        self.password = password
        self.email = email

    @classmethod
    def random(cls):
        from random import randint
        return cls(email_login="user" + str(randint(0, 1000000)),
                   password="pass" + str(randint(0, 1000000)),
                   email="user+" + str(randint(0, 1000000)) + "@gmail.com")















