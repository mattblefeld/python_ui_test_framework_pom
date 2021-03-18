from selenium.webdriver.common.by import By
from framework.basepage import BasePage


class LoginPage(BasePage):

    username_input = [By.ID, "username"]
    password_input = [By.ID, "password"]
    submit_button = [By.XPATH, "//*[@id='login']/button"]
    message = [By.ID, "flash"]
    logout = [By.XPATH, "//*[@id='content']//a[contains(., 'Logout')]"]

    def input_username(self, text):
        self.type_text(self.username_input, text)

    def input_password(self, text):
        self.type_text(self.password_input, text)

    def click_submit_button(self):
        self.click_(self.submit_button)

    def login_with(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_submit_button()

    def get_message_text(self):
        msg = self.get_text(self.message)
        return msg
