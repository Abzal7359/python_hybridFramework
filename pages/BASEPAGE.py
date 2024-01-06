from selenium.webdriver.common.by import By


class BASEPAGE:
    def __init__(self, driver):
        self.driver = driver

    def type(self, text, locator, locator_type):
        global element
        if locator_type == "xpath":
            element = self.driver.find_element(By.XPATH, locator)

        if locator_type == "id":
            element = self.driver.find_element(By.ID, locator)

        if locator_type == "name":
            element = self.driver.find_element(By.NAME, locator)

        element.clear()
        element.send_keys(text)
