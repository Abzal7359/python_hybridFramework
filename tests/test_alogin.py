
import pytest

from pages.LoginPage import LoginPage
from utilites import ReadConfigurations


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_Login_with_valid_credentials(self, setup_and_teardown):
        email = ReadConfigurations.read_configurarion("login cred", "email")
        password = ReadConfigurations.read_configurarion("login cred", "password")
        self.driver = setup_and_teardown
        LP = LoginPage(self.driver)
        assert LP.login(email, password)
