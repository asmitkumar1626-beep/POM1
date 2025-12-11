from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from utilities.base_page import Basepage

class Dashboard(Basepage):
    BACKPACK=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    LIGHT=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
    dropdown=(By.XPATH,"//select[@class='product_sort_container']")
    SHIRT=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
    Cart=(By.XPATH,"//a[@class='shopping_cart_link']")

    def add(self):
        self.click(self.BACKPACK)
        self.click(self.LIGHT)
        dropdown=self.wait.until(EC.presence_of_element_located(self.dropdown))
        select=Select(dropdown)
        select.select_by_visible_text("Price (low to high)")
        self.click(self.SHIRT)
    def gotocart(self):
        self.click(self.Cart)

