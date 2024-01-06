import random

import pytest
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_and_teardown")
class TestMyInvestments:

    def test_AddReferral_and_validate(self, setup_and_teardown):
        global product_names
        self.driver = setup_and_teardown
        #//p[@class='product-name']
        self.driver.find_element(By.XPATH,"(//a[normalize-space()='My Investments'])[1]").click()
        time.sleep(2)
        l=self.driver.find_elements(By.XPATH,"//p[@class='product-name']")
        product_names=[x.text for x in l]
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Refer & Earn'])").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Referral']").click()
        time.sleep(1)
        # Create a Faker object
        fake = Faker()
        # Generate a random full name
        name_of_referral = fake.name().replace(" ", "")
        # Generate a random phone number-like string
        fake_phone_number_with_zero = '0' + ''.join(random.choices('123456789', k=9))

        # Replace leading zero with another random digit (excluding zero)

        fake_phone_number_replaced = "9" + fake_phone_number_with_zero[
                                                         1:] if fake_phone_number_with_zero.startswith(
            '0') else fake_phone_number_with_zero
        amount = "1000"
        mail_id = name_of_referral + "@gmail.com"

        self.driver.find_element(By.XPATH, "//input[@name='fullName']").send_keys(name_of_referral)
        self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(fake_phone_number_replaced)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(mail_id)
        self.driver.find_element(By.XPATH, "//form/div[3]/div[1]/ng-select/div/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//ng-select/ng-dropdown-panel/div/div[2]/div/span").click()
        self.driver.find_element(By.XPATH, "//input[@name='amount']").send_keys(amount)
        self.driver.find_element(By.XPATH, "//span[text()='Send Refer']").click()
        time.sleep(2)

        val_name = self.driver.find_element(By.XPATH, "//tbody[1]/tr/td[2]").text

        assert val_name == name_of_referral

    def test_in_ReferEarn_payments(self, setup_and_teardown):
        self.driver = setup_and_teardown
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "form-select"))
        dropdown.select_by_visible_text("Payments")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//button[contains(@text,'')])[8]").click()
        dropdown_1 = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='ticketType']"))
        dropdown_1.select_by_index(0)
        dropdown_2 = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='profileId']"))
        dropdown_2.select_by_index(0)
        dropdown_3 = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='investmentId']"))
        options = [i.text for i in dropdown_3.options]
        # val=[[j in product_names for j in option.split()] for option in options]
        #below line to check the product names in options of dropdown
        val=[[j in k for k in options]for j in product_names]
        self.driver.find_element(By.XPATH,"(//div[normalize-space()='Cancel'])[1]").click()
        assert False not in val





