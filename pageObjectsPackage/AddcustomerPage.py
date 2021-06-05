import time
from selenium.webdriver.support.ui import Select


class AddCustomer():
    # Add customer Page. locator
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/i'
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = '//*[@id="Email"]'
    txtPassword_xpath = '//*[@id="Password"]'
    txtFirstName_xpath = '//*[@id="FirstName"]'
    txtLastName_xpath = '//*[@id="LastName"]'
    rdMaleGender_id = 'Gender_Male'
    rdFeMaleGender_id = 'Gender_Female'
    txtDob_xpath = '//*[@id="DateOfBirth"]'
    txtCompanyName_xpath = '//*[@id="Company"]'
    checkboxIsTaxExempt_xpath = '//*[@id="IsTaxExempt"]'
    # txtcustomerRoles_xpath = ''
    # lstitemAdministrators_xpath = ''
    # lstitemRegistered_xpath = ''
    # lstitemGuests_xpath = ''
    # lstitemVendors_xpath = ''
    drpmgrOfVendor_xpath = '//*[@id="VendorId"]'
    btSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFristname(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Femal":
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompname(self, companyname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(companyname)


    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.btSave_xpath).click()
