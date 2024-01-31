import string
import pytest
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
import random


class Test_0003_AddCustomer():
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()



    @pytest.mark.sanity
    def test_AddCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login successful***")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerIcon()
        self.addCust.clickOnCustomerMenuIcon()
        self.addCust.clickOnAddNewButton()

        self.logger.info("****** providing customer info ******")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Himanshu")
        self.addCust.setLastName("Agarwal")
        self.addCust.setGender("Male")
        self.addCust.managerVendor("Vendor 2")
        self.addCust.adminComment("Testing Application")
        self.addCust.clickOnSave()

        self.msg = self.driver.find_element_by_tag_name("body").text

        if "customer has been added successfully" in self.msg:
            assert True
        else:
            self.driver.save_screenshot("./screenshots/" + "test_a ddCustomer_scr.png")
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
