from Pages.BasePage import BasePage
from Locators.PageLocators import HomePageLocators
import time
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    URL = 'http://slotmachinescript.com/'
    VALUE_FIELDS = {'Bet':HomePageLocators.BET,
                    'TotalSpins': HomePageLocators.TOTAL_SPINS}

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators()

    def visit(self):
        self.driver.get(self.URL)
        return self

    def betSpinUp(self):
        self.findElement(self.locator.SPIN_UP).click()
        return self

    def betSpinDown(self):
        self.findElement(self.locator.SPIN_DOWN).click()
        return self

    def spinToPlay(self):
        btn = self.findElementToClick(self.locator.SPIN_BUTTON)
        btn.click()
        return btn

    def getValueOf(self, field):
        field = self.findElement(self.VALUE_FIELDS[field])
        return field.text

    def playAndWaitForGameEnd(self, timeout=30):
        btn = self.spinToPlay()
        end_time = time.time() + timeout
        while True:
            if not self.spinButtonDisabled(btn):
                return self
            else:
                time.sleep(1)
            if time.time() > end_time:
                break
        raise TimeoutException('Spin button is not more enabled')

    def betValueEquals(self, value):
        bet = self.getValueOf('Bet')
        return (int(value) == int(bet))

    def spinButtonDisabled(self, spinButton):
        return spinButton.get_attribute("class") == "disabled"
