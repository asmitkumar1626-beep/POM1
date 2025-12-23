from utilities.base_page import Basepage
from selenium.webdriver.common.by import By
class Login(Basepage):
    user=(By.XPATH,"//input[@id='user-name']")
    password=(By.XPATH,"//input[@id='password']")
    log_butt=(By.XPATH,"//input[@id='login-button']")

    def login(self):
        self.log.info("typing in the credentials")
        self.type(self.user,"standard_user")
        self.type(self.password,"secret_sauce")
        self.log.info("clicking on the login button")
        self.click(self.log_butt)
