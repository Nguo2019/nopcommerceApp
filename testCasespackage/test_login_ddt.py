import time
import pytest
from pageObjectsPackage.Loginpage import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import logGen
from utilities import XLUtils


class Test_TC002_Login_DDT:
    baseurl = readConfig.getAppURL()
    path = ".//TestData/LoginData.xlsx"
    logger = logGen.loggen()

    '''
    baseurl = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"
    以上内容，挪入新建的config.ini file了
    '''

    @pytest.mark.regression  # from Part 4 in youtbue
    def test_login_ddt(self, setup):  # when call setup, it will return driver
        self.logger.info("****************Test_002_Login_ddt*************")
        self.logger.info("******Verify Login DDT Test******")
        self.driver = setup  # when call setup, it will return driver
        self.driver.get(self.baseurl)

        self.lp = loginPage(self.driver)  # create an object to call the methods in Loginpage.py

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel", self.rows)

        lst_status = []  # empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', 'r', 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title ==expected_title:
                if self.exp=="Pass":
                    self.logger.info("Test is passed!")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***failed***")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif actual_title != expected_title:
                if self.exp == "Pass":
                    self.logger.info("****failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****passed****")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("***Login DDT test passed!***")
            self.driver.close()
            assert True
        else:
            self.logger.info("***Login DDT test failed!***")
            self.driver.close()
            assert False
        self.logger.info("******** End of Login DDT Test******")
        self.logger.info("******** Complete Test_TC002_Login_DDT ******")