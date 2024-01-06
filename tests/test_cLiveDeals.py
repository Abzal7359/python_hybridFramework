import pytest
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLiveDeals:
    def test_live_deals_visisble_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH,"(//a[normalize-space()='Live Deals'])[1]").click()
        deals_list = len(self.driver.find_elements(By.XPATH, "//app-live-deals-card/div/div"))
        assert deals_list

    def test_info_on_cards_is_displaying_inside_card(self, setup_and_teardown):
        self.driver = setup_and_teardown
        global minimum
        val = []
        values = []

        for i in range(1, 4):
            values.append(self.driver.find_element(By.XPATH,
                                                   f"(//app-live-deals-card/div/div[1]/div/div/div[1]/div[2]/div[2]/div/p)[{i}]").text)

        #     click on card
        self.driver.find_element(By.XPATH,
                                 "//app-live-deals-card/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/p[1]").click()

        time.sleep(2)

        # min in vestement
        min_invest = self.driver.find_element(By.XPATH, "//app-about-tab/div/div[1]/div[3]/span").text
        amount = self.driver.find_element(By.XPATH,
                                          "//app-product-details/div[2]/div/div[2]/div/div/div/div/ngx-slider/span[9]").text

        parts = min_invest.split()
        numeric_part = parts[1]


        # # Remove the currency symbol and convert to an integer
        numeric_value = int(numeric_part)

        # # Convert the numeric value to digits by multiplying by 100,000
        in_digits = str(numeric_value * 100000)
        val.append(min_invest == values[0] and amount == in_digits)
        # # expected ipr
        ipr = self.driver.find_element(By.XPATH, "//app-about-tab/div/div[2]/div[3]/span").text
        val.append(ipr == values[1])
        # # returns
        ret = self.driver.find_element(By.XPATH, "//app-about-tab/div/div[2]/div[4]/span").text
        slider_return = self.driver.find_element(By.XPATH,
                                                 "(//app-product-details/div[2]/div/div[2]/div/div/div/div/ngx-slider/span[9])[2]").text
        val.append(ret == values[2] and str(slider_return) in values[2])
        minimum = values[0]
        assert False not in val

    def test_bank_details_inside_card_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Bank Details']").click()
        time.sleep(2)
        l=[self.driver.find_element(By.XPATH,"//div[normalize-space()='Account Name']").is_displayed(),
           self.driver.find_element(By.XPATH,"//div[normalize-space()='Bank Name']").is_displayed(),
           self.driver.find_element(By.XPATH,"//div[normalize-space()='Account No']").is_displayed(),
           self.driver.find_element(By.XPATH,"//div[normalize-space()='IFSC Code']").is_displayed(),
           self.driver.find_element(By.XPATH,"//div[normalize-space()='Branch']").is_displayed()]
        assert False not in l

    def test_express_interest_showing_minimum_amount_after_entering_onedigit(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Express Interest']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[contains(@class,'modal')]").send_keys("1",Keys.ENTER)
        c= self.driver.find_element(By.XPATH, "//form/div[1]/div/div").text.__contains__(minimum)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
        assert c


