from selenium import webdriver
import unittest
from Pages.HomePage import HomePage
import sys
import logging
from selenium.webdriver.chrome.options import Options


class Slotmachine1_Test(unittest.TestCase):

    def setUp(self):
        self.driverPath = r'.\lib\chromedriver.exe'
        options = Options()
        options.add_argument('--window-size=1024x768')
        self.driver = webdriver.Chrome(executable_path=self.driverPath, chrome_options=options,
                                       service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

    def test_01_checkBetValues(self):
        expexted_bets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        logging.info('Test bet buttons and calculations')
        homePage = HomePage(self.driver)
        homePage.visit()
        for expexted_bet in expexted_bets:
            if expexted_bet == 1:
                assert homePage.betValueEquals(value = expexted_bet), f'Invalid value of bet, expected value: {expexted_bet}'
            else:
                homePage.betSpinUp()
                assert homePage.betValueEquals(value = expexted_bet), f'Invalid value of bet, expected value: {expexted_bet}'
        for expexted_bet in reversed(expexted_bets):
            if expexted_bet != 10:
                homePage.betSpinDown()
                assert homePage.betValueEquals(value = expexted_bet), f'Invalid value of bet, expected value: {expexted_bet}'

    def test_02_checkSpinButton(self):
         logging.info('Test if SpinButton is disabled while game')
         homePage = HomePage(self.driver)
         homePage.visit()
         spinButton = homePage.spinToPlay()
         assert homePage.spinButtonDisabled(spinButton), 'SpinButton is not disabled while game'

    def test_03_testCreditsCalculation(self):
        logging.info('Play for 5 credits and chceck if Total Spins value have been reduced')
        homePage = HomePage(self.driver).visit()
        start_credits = int(homePage.getValueOf('TotalSpins'))
        homePage.betSpinUp().betSpinUp().betSpinUp().betSpinUp().spinToPlay()
        credits_after_spin = int(homePage.getValueOf('TotalSpins'))
        expected_credits = start_credits - 5
        assert expected_credits == credits_after_spin , f'Credits are invalid calculated, expected value {expected_credits}, given {credits_after_spin}'

    def test_04_checkBetValueAfterGame(self):
        logging.info('Play for 3 credits and chceck if Bet value did not back to default 1 after game end')
        homePage = HomePage(self.driver).visit().betSpinUp().betSpinUp().playAndWaitForGameEnd()
        bet = int(homePage.getValueOf('Bet'))
        assert bet == 3 , f'Bet value is {bet} , expected value 3'

    def tearDown(self):
        if sys.exc_info()[0]:
            # Save screenshot if test is failed
            self.driver.save_screenshot(str(self.id()) + '.png')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
