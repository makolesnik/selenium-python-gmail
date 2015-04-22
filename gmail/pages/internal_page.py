from page import Page
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException


class InternalPage(Page):

    @property
    def click_write_email(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='T-I J-J5-Ji T-I-KE L3']")))
        return self.driver.find_element_by_xpath(".//*[@class='T-I J-J5-Ji T-I-KE L3']").click()

    @property
    def drafted_emails(self):
        self.driver.get("https://mail.google.com/mail/u/1/#drafts")
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='aio UKr6le']")))
        return self.driver.find_element_by_xpath(".//*[@class='aio UKr6le']").click()
        """
    def logout_link(self):
        return self.driver.get("https://mail.google.com/mail/logout?")

    def accept_alert_if_present(self):
        try:
            self.driver.switch_to_alert().accept()
        except (NoAlertPresentException, WebDriverException):
            pass
        finally:
            self.driver.switch_to_default_content()

    def email_subject(self, email_subject):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[text()='%s']" % email_subject)))
        return self.driver.find_elements_by_xpath(".//*[text()='%s']" % email_subject)

    def email_from(self, email_from):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@email='%s']" % email_from)))
        return self.driver.find_elements_by_xpath(".//*[@email='%s']" % email_from)

    def email_body(self, email_body):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[contains(.,'%s')]" % email_body)))
        return self.driver.find_elements_by_xpath(".//*[contains(.,'%s')]" % email_body)

    def emails_received(self, user_from, email):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[contains(.,'%s')]/span[contains(.,'%s')] | //td[contains(.,'%s')]" % (email.subject, email.body, user_from.email_login))))
        self.driver.find_elements_by_xpath(".//*[contains(.,'%s')]/span[contains(.,'%s')] | //td[contains(.,'%s')]" % (email.subject, email.body, user_from.email_login))

    def open_email_received(self, email_subject):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span/b[text()='%s']" % email_subject)))
        return self.driver.find_element_by_xpath("//span/b[text()='%s']" % email_subject).click()

    @property
    def get_page_title(self):
        return self.driver.find_element_by_css_selector("html.aAX head title").text

    def get_logged_user(self, user):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[contains(.,'%s')]" % user)))
        return self.driver.find_elements_by_xpath(".//*[contains(.,'%s')]" % user)

    def hover_on_attachment_by_file_name(self, file_name):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[starts-with(text(),'%s')]" % file_name)))
        attached_file = self.driver.find_element_by_xpath(".//*[starts-with(text(),'%s')]" % file_name)
        hover = ActionChains(self.driver).move_to_element(attached_file)
        hover.perform()

    def find_attachment_by_file_name(self, file_name):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[starts-with(text(),'%s')] | //span[text()='%s']" % file_name)))
        return self.driver.find_elements_by_xpath(".//*[starts-with(text(),'%s')] | //span[text()='%s']" % file_name)

    def attachment_size_in_kb(self, file_name, file_size_in_kb):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[text()='%s'] | //span[contains(.,'%s')]" % (file_name, file_size_in_kb))))
        return self.driver.find_elements_by_xpath(".//*[text()='%s'] | //span[contains(.,'%s')]" % (file_name, file_size_in_kb))

    def attachment_size_in_mb(self, file_name, file_size_in_mb):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[text()='%s'] | //span[contains(.,'%s')]" % (file_name, file_size_in_mb))))
        return self.driver.find_elements_by_xpath(".//*[text()='%s'] | //span[contains(.,'%s')]" % (file_name, file_size_in_mb))

    @property
    def is_this_page(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@role='navigation']")))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False