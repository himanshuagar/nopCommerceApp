import time

from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.AddCustomerPage import AddCustomer


class Test_SearchCustomerByEmail_004:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerIcon()
        self.addCust.clickOnCustomerMenuIcon()

        self.searchCust=SearchCustomer(self.driver)
        self.searchCust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCust.clickSearch()
        time.sleep(5)
        status= self.searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert  True == status
        self.logger.info("*****TC_searchCustomerByEmail is passed****")
