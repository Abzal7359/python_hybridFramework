import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_and_teardown")
class TestMyInvestments:
    def test_check_investmentIDS_visible_in_raise_ticket_dropdown(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "//a[normalize-space()='My Investments']").click()
        time.sleep(1)
        ll = len(self.driver.find_elements(By.XPATH,
                                           "(//app-my-investments/div/div[2]/div/div/div/div/div[2]/div/div/div/div)"))
        id = []
        name = self.driver.find_element(By.XPATH,
                                        "(//app-my-investments/div/div[2]/div/div/div/div/div[2]/div/div/div/div)").get_attribute(
            "title")
        for i in range(1, ll + 1):
            element = self.driver.find_element(By.XPATH,
                                               f"(//app-my-investments/div/div[2]/div/div/div/div/div[2]/div/div/div/div)[{i}]")
            namee = element.get_attribute("title")
            if namee == name:
                id.append(self.driver.find_element(By.XPATH,
                                                   f"(//app-my-investments/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/p)[{i}]").text)

        self.driver.find_element(By.XPATH, "//img[@class='help-icon-chevron']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Support']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Raise Ticket']").click()
        drop = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='profileId']"))
        drop.select_by_visible_text(name)

        id_drop = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='investmentId']"))

        # Get all the options in the dropdown
        all_options = [option.text for option in id_drop.options]
        flag = []
        for value in range(len(id)):
            flag.append(id[value] in all_options[value])  # line check the ids in dropdown

        self.driver.find_element(By.XPATH, "//div[normalize-space()='Cancel']").click()
        assert False not in flag
