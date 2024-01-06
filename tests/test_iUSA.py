import pytest
import time

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestUSA:
    def test_convert_to_USA_check_everything_converted_to_dollar(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "//*[@id='menu-button']/span").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='USA']").click()
        time.sleep(4)
        val = []
        # in dashboard validation $
        TE = self.driver.find_element(By.XPATH,
                                      "//app-dashboard/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div/h4").text
        val.append("$" in TE)

        LD=self.driver.find_elements(By.XPATH,"//p[contains(normalize-space(),'$')]")
        for i in LD:
            val.append("$" in i.text)

        # in Leads Page validation $
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Live Deals'])[1]").click()
        time.sleep(2)
        LDS = self.driver.find_elements(By.XPATH, "//p[contains(normalize-space(),'$')]")
        for i in LDS:
            val.append("$" in i.text)

        #click one deal
        self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'$')]").click()
        time.sleep(2)
        val.append("$" in self.driver.find_element(By.XPATH, "//app-about-tab/div/div[1]/div[3]/span").text)
        DS = self.driver.find_elements(By.XPATH, "//app-product-details/div[2]/div/div[2]/div/div/div[4]/div/div[1]")
        for i in DS:
            val.append("$" in i.text)


        #inside expected earnigns
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Expected Earnings']").click()
        time.sleep(2)
        for i in range(3,6):
            val.append("$" in self.driver.find_element(By.XPATH, f"//tbody/tr[1]/td[{i}]").text)

        self.driver.find_element(By.XPATH, "//*[@id='menu-button']/span").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='INDIA']").click()
        time.sleep(4)

        assert False not in val



