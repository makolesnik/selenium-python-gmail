# -*- coding: utf-8 -*-
import pytest
from gmail.model.user import User
from gmail.model.email import Email
from gmail.conftest import data_provider
import os
import time

base_dir = os.path.dirname(os.path.dirname(__file__))
login_data = data_provider('pass.csv', base_dir +'/tests/')

@pytest.mark.parametrize("login,password,login1,password1", login_data)
def test_login_with_valid_credentials(app, login, password, login1, password1):
    user = User(email_login=login, password=password)
    app.login(user)
    app.ensure_is_logged_in()
    app.ensure_is_logged_in_as(user)
    app.logout()




