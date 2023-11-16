import time

from selenium.webdriver.support.ui import Select


class AddCustomer:
    customerIcon_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customerMenuIcon_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addNewButton_xpath = "//a[@class='btn btn-primary']"
    emailTextBox_id = "Email"
    passwordTextBox_id = "Password"
    firstName_id = "FirstName"
    lastName_id = "LastName"
    maleGender_id = "Gender_Male"
    femaleGender_id = "Gender_Female"
    dateOfBirth_xpath = "//input[@id='DateOfBirth']"
    companyName_Id = "Company"
    customerRoles_xpath = "//div[@class='input-group-append input-group-required']"
    lstItemAdministrator_xpath = "//li[contains(text(),'Administrators')]"
    vendor_xpath = "//select[@id='VendorId']"
    ipAddress = "SearchIpAddress"
    adminContent_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerIcon(self):
        self.driver.find_element_by_xpath(self.customerIcon_xpath).click()

    def clickOnCustomerMenuIcon(self):
        self.driver.find_element_by_xpath(self.customerMenuIcon_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element_by_xpath(self.addNewButton_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.emailTextBox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.passwordTextBox_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_id(self.firstName_id).send_keys(firstname)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.lastName_id).send_keys(lastName)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.maleGender_id).click()
        else:
            self.driver.find_element_by_id(self.femaleGender_id).click()

    def setCustomerRoles(self):
        self.driver.find_element_by_xpath(self.customerRoles_xpath).click()
        self.driver.find_element_by_xpath(self.lstItemAdministrator_xpath).click()

    def managerVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.vendor_xpath))
        drp.select_by_visible_text(value)

    def adminComment(self,content):
        self.driver.find_element_by_id(self.adminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

