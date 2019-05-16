from selenium.webdriver.common.by import By


class HomePageLocators():

    SPIN_UP = (By.ID, ('betSpinUp'))
    SPIN_DOWN = (By.ID, ('betSpinDown'))
    SPIN_BUTTON = (By.ID, ('spinButton'))
    BET = (By.ID, ('bet'))
    TOTAL_SPINS = (By.ID, ('credits'))
