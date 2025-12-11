from utilities.base_page import Basepage
from selenium.webdriver.common.by import By
class Login(Basepage):
    user=(By.XPATH,"//input[@id='user-name']")
    password=(By.XPATH,"//input[@id='password']")
    log_butt=(By.XPATH,"//input[@id='login-button']")

    def login(self,username,password):
        self.type(self.user,"standard_user")
        self.type(self.password,"secret_sauce")
        self.click(self.log_butt)
