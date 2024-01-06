import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilites import ReadConfigurations


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def setup_and_teardown(request):
    url = ReadConfigurations.read_configurarion("basic info", "url")
    browser = ReadConfigurations.read_configurarion("basic info", "browser")
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    yield driver
    driver.find_element(By.XPATH,"//*[@id='page-topbar']/div/div[2]/div[4]/button/ngx-avatars/div/div").click()
    # driver.execute_script("arguments[0].click()",e)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='Sign Out']").click()
    # driver.execute_script("arguments[0].click()", z)
    time.sleep(2)
    driver.quit()


@pytest.fixture(autouse=True)
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
