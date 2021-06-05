import pytest
import time

from pageObjectsPackage.Loginpage import loginPage
from pageObjectsPackage.AddcustomerPage import AddCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import logGen
import string
import random

@pytest.mark.sanity  # from Part 4 in youtbue
class Test_003_AddCustomer:
    baseurl = readConfig.getAppURL()
    username = readConfig.getUserName()
    password = readConfig.getPassWord()
    logger = logGen.loggen()

    def test_AddCustomer(self, setup):
        self.logger.info("*************Test_003_AddCustomer********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login successful****")

        self.logger.info("******starting Add customer Test***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.logger.info("***to click  customer item***")
        time.sleep(5)
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("***Providing customer info***")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('pw123')
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender('Male')
        self.logger.info("***to input first name*****")
        self.addcust.setFristname('first')
        self.logger.info("***to input last  name*****")
        self.addcust.setLastname('last')
        self.logger.info("***to input dom*****")
        self.addcust.setDob("7/5/1985")
        self.addcust.setCompname('QA.inc')
        self.addcust.setManagerOfVendor('Vendor 1')
        self.addcust.clickSave()

        self.logger.info("***Saving customer info*****")
        self.logger.info("***Add customer validation***")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************Add customer Test Passed*************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("*********Add customer Test Failed!*********")
            assert True == False

        self.driver.close()
        self.logger.info("********Ending  Test_003_AddCustomer  Test")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
