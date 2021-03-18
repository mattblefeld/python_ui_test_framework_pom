"# python_ui_test_framework_pom"

### Introduction
This is a basic UI test framework, designed using the page object model pattern. 
It uses python, selenium webdriver, and pytest to load the browsers and run the tests.

The page object model approach, when using selenium, allows for a scalable, resilient, and maintainable test framework. 
The use of pytest, and specifically the use of it's markers, provides the ability to build test suites that can be easily integrated into CI/CD environments, like Jenkins.


### How To Run The Tests
Prerequisites: Python 3, Chrome browser, and Chromedriver

Download chrome browser: https://www.google.com/chrome/

or

`sudo apt-get install chromium-browser`

Download chromedriver (this must match the chrome version you install above):  https://chromedriver.chromium.org/downloads

or

`sudo apt-get install chromedriver`

Go to the root of this project and type the following:

`pip install -r requirements.txt`

`cd basic_pom_framework/tests`

After this next command, test collection should begin and a chrome browser should load and start performing the two tests that should be collected.

`pytest -m "login"`

