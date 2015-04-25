# -*- coding: utf-8 -*-
from gmail.pages.internal_page import InternalPage
from gmail.pages.login_page import LoginPage
from gmail.pages.email_page import EmailPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import time
from selenium.webdriver.common.keys import Keys


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 20)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.email_page = EmailPage(driver, base_url)

    def go_to_sign_in_form(self):
        lp = self.login_page
        if lp.sign_in_links:
            lp.sign_in_links[0].click()

    def deselect_stay_signed_in(self):
        lp = self.login_page
        if lp.stay_signed_in_checkbox.is_selected():
            lp.stay_signed_in_checkbox.click()

    def delete_all_cookies(self):
            self.delete_all_cookies()

    def login(self, user):
        lp = self.login_page
        lp.email_field.clear()
        lp.email_field.send_keys(user.email_login)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        if lp.stay_signed_in_checkbox.is_selected():
            lp.stay_signed_in_checkbox.click()

        lp.submit_button.click()

    def ensure_is_logged_in(self):
        ip = self.internal_page
        assert ip.is_this_page

    def ensure_is_logged_in_as(self, user):
        ip = self.internal_page
        gmail = user.email_login+"@gmail.com"
        assert len(ip.get_logged_user(gmail)) > 0

    def create_new_email(self, email):
        ip = self.internal_page
        assert ip.is_this_page
        ip.click_write_email
        ep = self.email_page
        assert ep.is_this_page
        ep.to_field.clear
        ep.to_field.send_keys(email.to)
        ep.subject_field.clear
        ep.subject_field.send_keys(email.subject)
        ep.body_field.clear
        ep.body_field.send_keys(email.body)
        time.sleep(2)

    def attach_file1(self, file_path):
        ep = self.email_page
        ep.attach_field.send_keys(file_path)

    def attach_file(self, email):
        for _file in email.attachment:
            ep = self.email_page
            ep.attach_file_to_message(_file)

    def ensure_file_is_attached(self, email):
        ep = self.email_page
        _list = []
        is_attached = False
        for element in ep.upload_info:
            _list.append(element.text)
        for i in _list:
            for _i in email.file_name:
                if _i in i:
                    is_attached = True
        assert is_attached

    def ensure_message_is_present(self, text):
        ep = self.email_page
        _list = []
        is_present = False
        for element in ep.send_message:
            _list.append(element.text)
        for i in _list:
            if text in i:
                is_present = True
        assert is_present

    def ensure_email_is_sent(self):
        ep = self.email_page
        assert len(ep.sent_message) > 0

    def ensure_email_is_received(self, user, email):
        ip = self.internal_page
        assert len(ip.email_subject(email.subject)) > 0
        assert len(ip.email_from(user.email_login+"@gmail.com")) > 0
        assert len(ip.email_body(email.body[:10])) > 0

    def ensure_email_is_drafted(self, user, email):
        ip = self.internal_page
        ip.drafted_emails
        assert len(ip.email_subject(email.subject)) > 0
        assert len(ip.email_from(user.email_login+"@gmail.com")) > 0
        assert len(ip.email_body(email.body[:10])) > 0

    def save_and_close_email(self):
        ep = self.email_page
        ep.save_and_close_button.click()

    def send_email(self):
        ep = self.email_page
        ep.send_button.click()

    def open_received_email(self, email):
        ip = self.internal_page
        ip.open_email_received(email.subject)

    def check_received_attachment_in_kb(self, file_name, file_size):
        ep = self.email_page
        assert ep.is_this_file(file_name)
        ip = self.internal_page
        ip.hover_on_attachment_by_file_name(file_name)
        file_size_in_kb_exists = len(ip.attachment_size_in_kb(file_name, file_size)) > 0
        assert file_size_in_kb_exists

    def check_received_attachment_in_mb(self, file_name, file_size):
        ep = self.email_page
        assert ep.is_this_file(file_name)
        ip = self.internal_page
        ip.hover_on_attachment_by_file_name(file_name)
        file_size_in_mb_exits = len(ip.attachment_size_in_mb(file_name, file_size)) > 0
        assert file_size_in_mb_exits

    def logout(self):
        ip = self.internal_page
        ip.logout_link()
        ip.accept_alert_if_present()

    def ensure_is_not_logged_in(self):
        assert self.login_page.is_this_page
