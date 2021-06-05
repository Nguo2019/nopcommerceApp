import time
from selenium.webdriver.support.ui import Select


class SearchCustomer:
    # Search customer Page. locator
    txtEmailsearch_id = 'SearchEmail'
    txtFirstnamesearch_id = 'SearchFirstName'
    txtLastnamesearch_id = 'SearchLastName'
    txtCompanyserach_id = 'SearchCompany'
    btnSearch_id = 'search-customers'

    tblSearchResults_xpath = ''
    table_xpath = '//*[@id="customers-grid"]'
    tableRows_xpath = '//*[@id="customers-grid"]/tbody/tr'
    tableColumns_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmailsearch_id).clear()
        self.driver.find_element_by_id(self.txtEmailsearch_id).send_keys(email)

    def setFirstName(self, fname):
        self.find_element_by_id(self.txtFirstnamesearch_id).cear()
        self.find_element_by_id(self.txtFirstnamesearch_id).send_keys(fname)

    def setLastName(self, lname):
        self.find_element_by_id(self.txtLastnamesearch_id).cear()
        self.find_element_by_id(self.txtLastnamesearch_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    # for 1st  test case search by email

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[2]')
            if emailid == email:
                flag = True
                break
        return flag

    # for 2nd test case search by name
    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]')
            if name == Name:
                flag == True
                break
        return flag
