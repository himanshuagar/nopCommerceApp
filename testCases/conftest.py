import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    else:
        raise ValueError("Unsupported browser specified")
    return driver


def pytest_addoption(parser):  # this will get value from CLI hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")


# Generate HTML Report


# Hook to add Environment information to HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Himanshu'


# Hook to delete environment info HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
