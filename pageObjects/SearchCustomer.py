class SearchCustomer:
    Email_id = "SearchEmail"
    firstName_id = "SearchFirstName"
    lastName_id = "SearchLastName"
    btn_search_id = "search-customers"

    tblSearchResult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.Email_id).clear()
        self.driver.find_element_by_id(self.Email_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.firstName_id).clear()
        self.driver.find_element_by_id(self.firstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.lastName_id).clear()
        self.driver.find_element_by_id(self.lastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def getNoRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoColumn(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailId = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailId == email:
                flag = True
                break
            return flag
