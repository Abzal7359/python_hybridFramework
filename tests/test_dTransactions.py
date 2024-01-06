import pytest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestTransactions:
    def test_payments_got_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Transactions'])[1]")
        (a
         .move_to_element(m)
         .move_to_element(self.driver.find_element(By.XPATH, "(//a[normalize-space()='Payments'])[1]"))
         .click()
         .perform())
        time.sleep(1)
        z = self.driver.find_element(By.XPATH, "//span[@class='headerText']").text

        assert z == "Track your payment history"

    def test_MyEarnings_got_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Transactions'])[1]")
        (a
         .move_to_element(m)
         .move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='My Earnings']"))
         .click()
         .perform())
        time.sleep(1)
        z = self.driver.find_element(By.XPATH, "//span[@class='headerText']").text

        assert z == "Track your earnings on your Investments"

    def test_tax_center_got_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Transactions'])[1]")
        (a
         .move_to_element(m)
         .move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='Tax Center']"))
         .click()
         .perform())
        time.sleep(1)
        z = self.driver.find_element(By.XPATH, "//span[@class='headerText']").text

        assert z == "Stay informed and manage your tax-related matters efficiently"
