from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        print("Launching Chrome browser")

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver")
        print("Launching Firefox browser")
    # if you forget to pass browser when using command, it will pop error. so we set up a default browser here.
    # pytest -v -s testCasespackage/test_login.py --browser chrome
    else:
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        print("Launching default browser chrome")

    return driver


# in order to use firefox browser
def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

############# Pytest HTML report#############
# It is hook for Adding Environment info to html report.
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Nerissa'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)