# -*- coding: utf-8 -*-
import pytest
from gmail.model.user import User
from gmail.model.email import Email
from gmail.conftest import data_provider
import os
import time

base_dir = os.path.dirname(os.path.dirname(__file__))
send_email_data = data_provider('send_email.csv', base_dir +'//tests//test_data//')


@pytest.mark.parametrize("login,password,login1,password1,subject,body", send_email_data)
def test_create_email(app, login, password, login1, password1, subject, body):
    user = User(email_login=login, password=password)
    email = Email(to=login1+"@gmail.com", subject=subject, body=body,
                  attachment=[base_dir+'/tests/image.png', base_dir+'/tests/pass.csv'],
                  file_name=["image.png", "pass.csv"])
    app.login(user)
    app.ensure_is_logged_in()
    app.create_new_email(email)
    app.attach_file(email)
    app.ensure_file_is_attached(email)
    app.save_and_close_email()
    app.ensure_email_is_drafted(user, email)
    app.logout()
    app.ensure_is_not_logged_in()




