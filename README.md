# selenium-python-gmail

Simple Gmail tests with python and selenium

# How to start:

install python 2.7

install virtualenv

install pip

install selenium

install pytest

make directory for project and clone there this project:

git clone https://github.com/mkpythonanywhereblog/selenium-python-gmail.git


# How to run your first test from PyCharm (IDE):

install PyCharm  


open "selenium-python-gmail" directory in PyCharm

go to "Run" > "Edit Configurations". Select "Add New Configuration" > "Python Tests" > "py.test".

Name: name for command to run py.test with the test 

Example: pytest in login_test.py

Target: path\to\login_test.py

Example: C:\Users\user\Documents\DEMO\selenium-python-gmail\gmail\tests\login_test.py

Select python interpreter (optional)

Apply changes


To run test go to "Run" > "Run pytest in login_test.py"


If you have an issue with running tests try to change path to csv files in the test.

Google Chrome is used by default, for more details about browsers please see conftest.py.
