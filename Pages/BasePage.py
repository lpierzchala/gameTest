from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator, timeout=30):
        '''Find element for given locator'''
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print('Timeout: Cannot find element defined by selector')
            return False

    def findElementToClick(self, locator, timeout=30):
        '''Find element for given locator and wait until it will be clickable'''
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print('Timeout: Cannot find element defined by selector')
            return False
