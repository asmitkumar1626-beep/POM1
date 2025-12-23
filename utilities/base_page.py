from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger_ import get_log

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.log=get_log(self.__class__.__name__)
    def type(self,locator,text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
