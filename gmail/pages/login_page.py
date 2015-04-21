from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class LoginPage(Page):

    @property
    def sign_in_links(self):
        return self.driver.find_elements_by_id("gmail-sign-in")

    @property
    def email_field(self):
        return self.driver.find_element_by_id("Email")

    @property
    def password_field(self):
        return self.driver.find_element_by_name("Passwd")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("signIn")

    @property
    def stay_signed_in_checkbox(self):
        return self.driver.find_element_by_id("PersistentCookie")


    @property
    def is_this_base_page(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "gmail-sign-in")))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False


    @property
    def is_this_page(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "gaia_loginform")))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

