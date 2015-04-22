# -*- coding: utf-8 -*-
import pytest
from gmail.model.application import Application
from selenium import webdriver
import csv
import os
import time


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="http://gmail.com", help="base URL")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="session")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()

    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)


def data_provider(fcsv, csvpath):
    if csvpath == '':
        pass
    else:
        os.chdir(csvpath)
    with open(fcsv, 'rb') as csvfile:
        test_data = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            test_data.append(tuple(row))
        print test_data
    csvfile.close
    return test_data


def base_dir():
    return os.path.dirname(os.path.dirname(__file__))
