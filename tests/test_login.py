from framework.pages.login_page import LoginPage
from framework.pages.site_selector_page import SiteSelectorPage
from framework.config.config import valid_username, valid_password, invalid_username, invalid_password
import pytest


@pytest.mark.login
class TestLogin:

    def test_valid_login(self, driver):
        """
        Purpose: To test that, when a user enters a valid username and password, that the authentication works and the user is greeted with a success message.
        """
        login_page = LoginPage(driver)
        site_page = SiteSelectorPage(driver)

        site_page.click_form_authentication_link()

        login_page.login_with(valid_username, valid_password)

        message = login_page.get_message_text()

        assert ("You logged into a secure area!" in message) is True

    def test_invalid_login(self, driver):
        """
        Purpose: To test that, when a user enters an invalid username and password, that the authentication works and the user is greeted with an error message.
        """
        login_page = LoginPage(driver)
        site_page = SiteSelectorPage(driver)

        site_page.click_form_authentication_link()

        login_page.login_with(invalid_username, invalid_password)

        message = login_page.get_message_text()

        assert ("Your username is invalid!" in message) is True
