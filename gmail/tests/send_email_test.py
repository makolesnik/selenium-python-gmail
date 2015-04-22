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
def test_send_email(app, login, password, login1, password1, subject, body):
    from_user = User(email_login=login, password=password)
    to_user = User(email_login=login1, password=password1)
    email = Email(to=login1+"@gmail.com", subject=subject, body=body,
                  attachment=[base_dir+'/tests/test_data/image.png', base_dir+'/tests/test_data/pass.csv'],
                  file_name=["image.png", "pass.csv"])

    app.login(from_user)
    app.ensure_is_logged_in()
    app.create_new_email(email)
    app.attach_file(email)
    app.ensure_file_is_attached(email)
    app.send_email()
    app.ensure_email_is_sent()
    app.logout()
    app.ensure_is_not_logged_in()
    app.login(to_user)
    app.ensure_is_logged_in()
    app.ensure_email_is_received(from_user, email)
    app.open_received_email(email)
    app.check_received_attachment_in_kb(email.file_name[1], "1")
    app.logout()
    app.ensure_is_not_logged_in()