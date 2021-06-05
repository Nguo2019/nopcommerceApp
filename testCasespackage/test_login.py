import pytest
from pageObjectsPackage.Loginpage import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import logGen


class Test_TC001_Login:
    '''
    baseurl = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"
    以上内容，挪入新建的config.ini file了
    '''
    baseurl = readConfig.getAppURL()
    username = readConfig.getUserName()
    password = readConfig.getPassWord()
    logger = logGen.loggen()

    # method1 in TC001
    @pytest.mark.regression  # from Part 4 in youtbue
    def test_homePageTitle(self, setup):

        self.logger.info("******Test_TC001******")
        self.logger.info("******Verify Home Page Title******")
        # created driver twice  so move it to conf.y and modify method from test_homePageTitle(self) to (self,setup)
        #  self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******Home Page Title test  is passed!******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******Home Page Title test  is failed!******")
            assert False

    # method2 in TC001
    @pytest.mark.sanity  # from Part 4 in youtbue
    @pytest.mark.regression  # from Part 4 in youtbue
    def test_login(self, setup):  # when call setup, it will return driver
        self.logger.info("******Title of Start Page  after logging in******")
        #  self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        self.driver = setup  # when call setup, it will return driver
        self.driver.get(self.baseurl)
        self.lp = loginPage(self.driver)  # create an object to call the methods in Loginpage.py
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******Login test is passed!******")
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******Login test is failed******")
            assert False
