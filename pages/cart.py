from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class CART(Basepage):
    CHECKOUT=(By.XPATH,"//button[@id='checkout']")

    def checkout(self):
        self.click(self.CHECKOUT)