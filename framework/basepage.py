from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_appear(self, locator, timer=30):
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.visibility_of_element_located(locator))

    def wait_until_text_appears(self, locator, text, timer=30):
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.text_to_be_present_in_element(locator, text))

    def get_element(self, locator):
        self.wait_for_element_to_appear(locator)
        return self.driver.find_element(locator[0], locator[1])

    def get_elements(self, locator):
        self.wait_for_element_to_appear(locator)
        return self.driver.find_elements(locator[0], locator[1])

    def is_element_visible(self, locator):
        try:
            return self.get_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_(self, url):
        self.driver.get(url)

    def click_(self, locator):
        self.wait_for_element_to_appear(locator)
        self.get_element(locator).click()

    def type_text(self, locator, text):
        self.wait_for_element_to_appear(locator)
        self.get_element(locator).send_keys(text)

    def clear_text(self, locator):
        self.wait_for_element_to_appear(self, locator)
        self.get_element(locator).clear()

    def get_text(self, locator):
        elem = self.get_element(locator)
        text = str(elem.text)
        if text == '':
            value = str(elem.get_attribute('value'))
            return value
        return text

    def set_checkbox(self, locator, state=True):
        """
        Purpose: To check if a checkbox is checked, and then set it to the state requested based on the current state.
        :param state: True for checked, False for unchecked
        """

        if state:
            if self.get_element(locator).is_checked():
                pass
            else:
                self.click_(locator)
        else:
            if self.get_element(locator).is_checked():
                self.click_(locator)
            else:
                pass
