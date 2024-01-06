import pytest
import time

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSettings:
    def test_password_and_phone_number(self, setup_and_teardown):

        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "(//div[@class='avatar-content'])[1]").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Settings']").click()
        password = self.driver.find_element(By.XPATH, "//section/div/h6").text
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Phone Number']").click()
        phone = self.driver.find_element(By.XPATH, "//form/div[1]/h6").text

        assert password == "Update your Password" and phone == "Update your Mobile Number"
        # Update your Password
#         //section/div/h6--//form/div[1]/h6
