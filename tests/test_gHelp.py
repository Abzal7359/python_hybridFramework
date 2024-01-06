import pytest
import time
from datetime import datetime
import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_and_teardown")
class TestHelp:

    def test_FAQs_getting_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "//img[@class='help-icon-chevron']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='FAQs']").click()
        l = len(self.driver.find_elements(By.XPATH, "//app-faq/div/div[1]/div/div/div/div[1]/button/img"))
        val = []
        for i in range(1, l + 1):
            self.driver.find_element(By.XPATH, f"(//app-faq/div/div[1]/div/div/div/div[1]/button/img)[{i}]").click()
            time.sleep(1)
            val.append(
                self.driver.find_element(By.XPATH, f"(//app-faq/div/div[1]/div/div/div/div[2]/p)[{i}]").is_displayed())
            self.driver.find_element(By.XPATH, f"(//app-faq/div/div[1]/div/div/div/div[1]/button/img)[{i}]").click()

        assert False not in val

    def test_Support_getting_displayed_or_not(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "//img[@class='help-icon-chevron']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Support']").click()
        z = self.driver.find_element(By.XPATH, "//span[@class='headerText']").text
        assert z == "Please contact our executives or Raise ticket"

    def test_Support_bookAppoinment_is_redirecting_to_calendly(self, setup_and_teardown):
        self.driver = setup_and_teardown
        val = []
        rangee = len(self.driver.find_elements(By.XPATH, "(//button[normalize-space()='Book Appointment'])"))
        for i in range(1, rangee + 1):
            original_window_handle = self.driver.current_window_handle

            self.driver.find_element(By.XPATH, f"(//button[normalize-space()='Book Appointment'])[{i}]").click()
            time.sleep(2)
            # Switch to the new tab
            for window_handle in self.driver.window_handles:
                if window_handle != original_window_handle:
                    self.driver.switch_to.window(window_handle)

            new_tab_url = self.driver.current_url
            val.append(new_tab_url.__contains__("https://calendly.com/"))
            # Close the new tab
            self.driver.close()

            # Switch back to the original tab
            self.driver.switch_to.window(original_window_handle)

        assert False not in val

    @pytest.mark.skip(reason="more tickets creating")
    def test_raise_ticket_and_validate_ticket_created(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Raise Ticket']").click()

        # ticket type selection
        drop = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='ticketType']"))
        drop.select_by_index(1)

        # userprofile selection
        dropp = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='profileId']"))
        dropp.select_by_index(1)

        # investment selection
        dro = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='investmentId']"))
        dro.select_by_index(1)

        # description writing
        self.driver.find_element(By.ID, "basicpill-address-input1").send_keys("query related payment")

        self.driver.find_element(By.XPATH, "//div[normalize-space()='Submit']").click()
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the date and time as "Mon DD, YYYY H:MM AM/PM"
        formatted_datetime = current_datetime.strftime("%b %d, %Y %#I:%M %p")

        time.sleep(1)
        val = self.driver.find_element(By.XPATH, "//tbody[1]/tr/td[5]").text

        assert formatted_datetime in val


    def test_openChat_and_valiadteChat_and_time(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.driver.find_element(By.XPATH,"//tbody/tr/td[8]/img").click()
        time.sleep(1)
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
        message = formatted_datetime + "testing"
        self.driver.find_element(By.XPATH,"(//textarea[@type='text-area'])[1]").send_keys(message,Keys.ENTER)
        time.sleep(2)
        _time = datetime.datetime.now().time()
        matted_time = _time.strftime("%I:%M %p").lstrip("0")
        ll=[]

        l=self.driver.find_elements(By.XPATH,"(//pre[contains(normalize-space(),'')])")
        for i in range (1,len(l)+1):
            t=self.driver.find_element(By.XPATH,f"(//pre[contains(normalize-space(),'')])[{i}]").text
            if t==message:
                timee=self.driver.find_element(By.XPATH,f"((//pre[contains(normalize-space(),'')])/following-sibling::small)[{i}]").text
                if timee== matted_time:
                    ll.append(True)
                    self.driver.find_element(By.XPATH,"(//img[@class='close'])[1]").click()
                    break
                else:
                    self.driver.find_element(By.XPATH, "(//img[@class='close'])[1]").click()
                    ll.append(timee)
                    ll.append(matted_time)
                    ll.append(False)
                    break

            else:
                pass
        assert False not in ll





    def test_search_ticket_by_ticket_number(self, setup_and_teardown):
        self.driver = setup_and_teardown
        # get ticket id
        ticket_id = self.driver.find_element(By.XPATH, "//tbody/tr/td[1]").text

        first_part = ""
        # Find the index of the last numeric character
        last_numeric_index = -1
        for i, char in enumerate(ticket_id):
            if char.isdigit():
                last_numeric_index = i

        # Split the string into two parts
        if last_numeric_index != -1:
            first_part = ticket_id[:last_numeric_index + 1]

        # input search
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Ticket Number']").send_keys(first_part,
                                                                                                        Keys.ENTER)
        time.sleep(2)
        z = first_part in self.driver.find_element(By.XPATH, "//tbody/tr/td[1]").text
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Clear filters']").click()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Ticket Number']").send_keys("",
        #                                                                                                 Keys.ENTER)
        time.sleep(2)

        assert z

    @pytest.mark.parametrize("filters", ["Closed", "Open","Overdue"])
    def test_ApplyStatusFilter_validate_filter_applied_or_not(self, setup_and_teardown, filters):
        self.driver = setup_and_teardown
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "//app-help-desk/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/ng-select/div/span").click()
        # self.driver.execute_script("arguments[0].click()", element_to_click)
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//div[normalize-space()='{filters}']").click()
        time.sleep(2)
        l = self.driver.find_elements(By.XPATH, "//tbody/tr/td[7]/span")
        val = []
        flag = True
        for i in l:
            if i.text == filters:
                pass
            else:
                flag = False
                val.append(flag)
                break
        self.driver.find_element(By.XPATH,
                                 "(//app-help-desk/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/ng-select/div/span)[2]").click()
        assert False not in val
