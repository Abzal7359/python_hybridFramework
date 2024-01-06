from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BASEPAGE import BASEPAGE


class LoginPage(BASEPAGE):
    def __init__(self, driver):
        super().__init__(driver)

        # Define element locators

    EMAIL_INPUT_NAME = "email"
    PASSWORD_INPUT_NAME = "password"
    SIGN_IN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign In']")
    SEND_OTP_BUTTON = (By.XPATH, "//button[normalize-space()='Send OTP']")
    OTP_INPUTS_XPATH = [
        "//ng-otp-input/div/input[1]",
        "//ng-otp-input/div/input[2]",
        "//ng-otp-input/div/input[3]",
        "//ng-otp-input/div/input[4]"
    ]
    VERIFY_BUTTON = (By.XPATH, "//button[normalize-space()='Verify']")
    DASHBOARD_LINK = (By.XPATH, "(//a[normalize-space()='Dashboard'])")

    def login(self, email, password):
        self.type(email, self.EMAIL_INPUT_NAME, "name")
        self.type(password, self.PASSWORD_INPUT_NAME, "name")
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()
        self.driver.find_element(*self.SEND_OTP_BUTTON).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Verification']")))
        for i in range(4):
            self.type("0", self.OTP_INPUTS_XPATH[i], "xpath")
        self.driver.find_element(*self.VERIFY_BUTTON).click()
        return self.driver.find_element(*self.DASHBOARD_LINK).is_displayed()
