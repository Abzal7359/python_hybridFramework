import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestDashboard:
    def test_dashboard_elements_are_present(self, setup_and_teardown):
        self.driver = setup_and_teardown
        # total earning present or not
        l = []
        l.append(self.driver.find_element(By.XPATH, "//span[normalize-space()='Total Earnings']").is_displayed())
        l.append(self.driver.find_element(By.XPATH, "//span[normalize-space()='Average IRR']").is_displayed())
        l.append(self.driver.find_element(By.XPATH, "//span[normalize-space()='Average Yield']").is_displayed())
        l.append(self.driver.find_element(By.XPATH, "//h3[normalize-space()='Live Deals']").is_displayed())
        lenn = len(self.driver.find_elements(By.XPATH, "//app-live-deals-card/div/div"))
        if lenn >= 1:
            l.append(True)

        assert False not in l

    def test_dashboard_totalEarnings_check_in_MYearnings(self, setup_and_teardown):
        self.driver = setup_and_teardown
        amount = self.driver.find_element(By.XPATH, "(//h4[contains(text(),'')])[2]").text
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Transactions'])[1]")
        (a
         .move_to_element(m)
         .move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='My Earnings']"))
         .click()
         .perform())
        time.sleep(1)
        showing_amount = self.driver.find_element(By.XPATH,
                                                  "(//span[normalize-space()='Total Earnings'])/../following-sibling::div/div").text
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Dashboard'])[1]").click()
        assert amount == showing_amount

    def test_tasks_showing_list_count_is_same_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        li = [len(self.driver.find_elements(By.XPATH, "//tasks/div/div[2]/ul/div/div"))]
        whole = []
        keys = []
        val = []
        for i in range(1, (li[0] + 1)):
            name = []
            name.append(self.driver.find_element(By.XPATH, f"(//tasks/div/div[2]/ul/div/div/li/div[1]/h4)[{i}]").text)
            key = len(self.driver.find_elements(By.XPATH, f"(//tasks/div/div[2]/ul/div[{i}]/div/li/div[2]/span/span)"))
            for j in range(1, key + 1):
                keys = []
                keys.append(self.driver.find_element(By.XPATH,
                                                     f"(//tasks/div/div[2]/ul/div[{i}]/div/li/div[2]/span/span)[{j}]").text)
            whole.append(name)
            whole.append(keys)
        self.driver.find_element(By.XPATH, "(//div[@class='avatar-content'])[1]").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Profiles']").click()

        for k in range(len(whole)):
            if k % 2 == 0:
                name = whole[k][0]
                ele = self.driver.find_element(By.XPATH,
                                               f"//app-profile-cards/section/div[2]/div/div/div/div[1]/div[2]/div/p[text()=' {name} ']")
                self.driver.execute_script("arguments[0].click()", ele)
                time.sleep(2)
            else:
                for l in range(1, len(whole[k]) + 1):
                    typ = whole[k][l - 1]
                    warn = self.driver.find_element(By.XPATH,
                                                    f"//app-profiles/div[2]/div/div[2]/ul/li/a/div/span[contains(text(),'{typ}')]/following-sibling::img")
                    red = warn.get_attribute('src')
                    val.append(red.__contains__("pending.svg"))

                self.driver.find_element(By.XPATH, "//li[text()='Profiles ']").click()
                time.sleep(2)
        time.sleep(2)
        assert li[0] == len(self.driver.find_elements(By.XPATH,
                                                      "//section/div[2]/div/div/div/div[4]/div[3]/div/div")) and False not in val
