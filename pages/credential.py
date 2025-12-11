from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Credentials(Basepage):
    USER=(By.XPATH,"//input[@id='first-name']")
    Lastname=(By.XPATH,"//input[@id='last-name']")
    Zipcode=(By.XPATH,"//input[@id='postal-code']")
    Continue=(By.XPATH,"//input[@id='continue']")

    def credentials(self):
        self.type(self.USER,"Asmit")
        self.type(self.Lastname,"kumar")
        self.type(self.Zipcode,"78451")
    def click_continue(self):
        self.click(self.Continue)