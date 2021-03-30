from selenium import webdriver
import os

# Variables to be used universally in the tests runs
url_to_test = "http://the-internet.herokuapp.com"

# test credentials
valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"

invalid_username = "invalid user"
invalid_password = "invalid password"

# get local working directory for screenshots
path_to_screenshots = ((os.getcwd()).strip("tests")) + "screenshots\\"


# Create the capabilities of the webdriver instance
def webdriverinstance():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument('--start-maximized')
    chromeoptions.add_argument('--disable-extensions')
    driver = webdriver.Chrome(chrome_options=chromeoptions)

    return driver
