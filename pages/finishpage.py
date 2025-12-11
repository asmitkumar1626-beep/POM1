from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage

class Finish(Basepage):
    TOTAL=(By.XPATH,"//div[@class='summary_total_label']")
    Finish=(By.XPATH,"//button[@id='finish']")

    def finsh(self):
        print(self.get_text(self.TOTAL))
        self.click(self.Finish)
