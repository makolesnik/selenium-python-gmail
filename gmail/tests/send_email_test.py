# -*- coding: utf-8 -*-
import pytest
from gmail.model.user import User
from gmail.model.email import Email
from gmail.conftest import data_provider
import os
import time

base_dir = os.path.dirname(os.path.dirname(__file__))
login_data = data_provider('pass.csv', base_dir +'/tests/')
message_data = data_provider('message.csv', base_dir +'/tests/')

@pytest.mark.parametrize("login,password,login1,password1", login_data)
@pytest.mark.parametrize("to,subject,body", message_data)
def test_send_email(app, login, password, login1, password1, to, subject, body):
    from_user = User(email_login=login, password=password)
    to_user = User(email_login=login1, password=password1)
    email = Email(to=to, subject=subject, body=body,
                  attachment=[base_dir+'/tests/message.csv', base_dir+'/tests/pass.csv'],
                  file_name=["message.csv", "pass.csv"])

    app.login(from_user)
    app.ensure_is_logged_in()
    app.create_new_email(email)
    app.attach_file(email)
    app.ensure_file_is_attached(email)
    app.send_email()
    app.ensure_email_is_sent()
    #app.ensure_message_is_present('Переглянути повідомлення')
    app.logout()
    app.ensure_is_not_logged_in()
    app.login(to_user)
    app.ensure_is_logged_in()
    app.ensure_email_is_received(from_user, email)

