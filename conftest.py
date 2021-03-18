import pytest
from framework.config.config import webdriverinstance, url_to_test, path_to_screenshots
from datetime import datetime
import os


@pytest.fixture()
def driver(request):
    driver = webdriverinstance()

    driver.get(url_to_test)

    def take_screenshot():
        print("The failure screenshot was saved here:" + path_to_screenshots)
        if not os.path.exists(path_to_screenshots):
            os.mkdir(path_to_screenshots)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M')
        driver.save_screenshot(path_to_screenshots + ('test_failure_' + request.node.name + '_{0}.png'.format(now)))

    yield driver

    if request.session.testsfailed > 0:
        request.session.testsfailed = 0
        take_screenshot()
        driver.quit()
    else:
        driver.quit()
