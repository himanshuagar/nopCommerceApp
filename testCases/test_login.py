import pytest

from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("*********Test001********")
        self.logger.info("******* verify home page title ********")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        self.title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            self.logger.error("******* verify home page title test failed ********")
            assert False

    def test_login(self, setup):
        self.logger.info("******* verify login test********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        print ("testing test_login newwwwwwwwww" )
        act_title = self.driver.title
        self.driver.close()

        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            self.logger.info("******* verify login test passed ********")
            assert True
        else:
            assert False
