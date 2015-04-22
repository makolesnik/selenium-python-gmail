# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from page import Page
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import time


class EmailPage(Page):

    @property
    def to_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='vO']")))
        return self.driver.find_element_by_xpath(".//*[@class='vO']")

    @property
    def subject_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='aoT']")))
        return self.driver.find_element_by_xpath(".//*[@class='aoT']")

    @property
    def body_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='Am Al editable LW-avf']")))
        return self.driver.find_element_by_xpath(".//*[@class='Am Al editable LW-avf']")

    @property
    def attach_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='a1 aaA aMZ']")))
        return self.driver.find_element_by_xpath(".//*[@class='a1 aaA aMZ']")

    @property
    def attach_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='a1 aaA aMZ']")))
        file_input = self.driver.find_element_by_xpath(".//*[@class='a1 aaA aMZ']")
        return self.driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_input)

    @property
    def send_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='T-I J-J5-Ji aoO T-I-atl L3']")))
        return self.driver.find_element_by_xpath(".//*[@class='T-I J-J5-Ji aoO T-I-atl L3']")

    @property
    def save_and_close_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='Ha']")))
        return self.driver.find_element_by_xpath(".//*[@class='Ha']")

    @property
    def save_status(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='oG aOy']")))
        return self.driver.find_element_by_xpath(".//*[@class='oG aOy']")

    @property
    def upload_info(self):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@class='dO']")))
        return self.driver.find_elements_by_xpath(".//*[@class='dO']")

    def find_upload_by_file_name(self, file_name):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@class='vI' and text()='%s']" % file_name)))
        return self.driver.find_elements_by_xpath(".//*[@class='vI' and text()='%s']" % file_name)

    def find_upload_by_file_size(self, file_size_as_number):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@class='vJ' and starts-with(text(),'(%s')]" % file_size_as_number)))
        return self.driver.find_elements_by_xpath(".//*[@class='vJ' and starts-with(text(),'(%s')]" % file_size_as_number)

    @property
    def sent_message(self):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@class='vh']")))
        return self.driver.find_elements_by_xpath(".//*[@class='vh']")

    def is_this_file(self, file_name):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[text()='%s']" % file_name)))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False


    @property
    def is_this_page(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='aYF']")))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    def attach_file_to_message(self, file_path):
         file_input = self.create_file_input_element()
         file_input.send_keys(file_path)
         self.dispatch_file_drag_event('dragenter', 'document', file_input)
         self.dispatch_file_drag_event('dragover', 'document', file_input)
         self.wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@class='aDa']")))
         drag_target = self.driver.find_element_by_xpath(".//*[@class='aDa']")
         self.dispatch_file_drag_event('drop', drag_target, file_input)
         #time.sleep(5)
         self.driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", file_input)

    def create_file_input_element(self):
         return self.driver.execute_script(
         "var input = document.createElement('input');"
         "input.type = 'file';"
         "input.style.display = 'block';"
         "input.style.opacity = '1';"
         "input.style['transform']='translate(0px, 0px) scale(1)';"
         "input.style['MozTransform']='translate(0px, 0px) scale(1)';"
         "input.style['WebkitTransform']='translate(0px, 0px) scale(1)';"
         "input.style['msTransform']='translate(0px, 0px) scale(1)';"
         "input.style['OTransform']='translate(0px, 0px) scale(1)';"
         "input.style.visibility = 'visible';"
         "input.style.height = '1px';"
         "input.style.width = '1px';"
         "if (document.body.childElementCount > 0) { "
         " document.body.insertBefore(input, document.body.childNodes[0]);"
         "} else { "
         " document.body.appendChild(input);"
         "}"
         "return input;"
         )

    def dispatch_file_drag_event(self, event_name, to, file_input_element):
         script =  "var files = arguments[0].files;" \
         "var items = [];" \
         "var types = [];" \
         "for (var i = 0; i < files.length; i++) {" \
         " items[i] = {kind: 'file', type: files[i].type};" \
         " types[i] = 'Files';" \
         "}" \
         "var event = document.createEvent('CustomEvent');" \
         "event.initCustomEvent(arguments[1], true, true, 0);" \
         "event.dataTransfer = {" \
         " files: files," \
         " items: items," \
         " types: types" \
         "};" \
         "arguments[2].dispatchEvent(event);"

         if isinstance(to, basestring):
            script = script.replace('arguments[2]', to)
            args = file_input_element, event_name,
         else:
            args = file_input_element, event_name, to
            self.driver.execute_script(script, *args)

