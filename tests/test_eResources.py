import pytest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("setup_and_teardown")
class TestResources:
    def test_blogs_getting_display_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Resources'])[1]")
        (a
         .move_to_element(m)
         .move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='Blogs']"))
         .click()
         .perform())
        time.sleep(1)
        z = len(self.driver.find_elements(By.XPATH, "//app-blogs/div[2]/div[2]/div/div"))

        assert z 

