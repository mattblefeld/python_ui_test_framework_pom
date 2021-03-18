from selenium.webdriver.common.by import By
from framework.basepage import BasePage


class SiteSelectorPage(BasePage):

    form_authentication_link = [By.XPATH, "//*[@id='content']//a[contains(., 'Form Authentication')]"]

    def click_form_authentication_link(self):
        self.click_(self.form_authentication_link)

