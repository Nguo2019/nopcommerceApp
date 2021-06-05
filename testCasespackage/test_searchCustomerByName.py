from pageObjectsPackage import Loginpage
from pageObjectsPackage import  AddcustomerPage
from pageObjectsPackage import SearchCustomerPage
from pageObjectsPackage.AddcustomerPage import AddCustomer
from pageObjectsPackage.Loginpage import loginPage
from pageObjectsPackage.SearchCustomerPage import SearchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import logGen
import pytest
import time

class test_TC005_SearchCustomerByName:
    baseurl = readConfig.getAppURL()
    username = readConfig.getUserName()
    password = readConfig.getPassWord()
    logger = logGen.loggen()

    @pytest.mark.regression  # from Part 4 in youtbue
    def test_searchCustomerByName(self, setup):
        self.logger.info("****start test_TC004_SearchCustomerByEmail******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()


        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login successful****")

        self.logger.info("****start  Search Customer By Name******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.logger.info("***to click  customer item***")
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("****start  search customer by emailID******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep()
        status = searchcust.searchCustomerByName("Victoria Teres")
        assert True == status
        self.logger.info("***************test_TC005_SearchCustomerByName**************")
        self.driver.close()




