from utilities.base_page import Basepage
from pages.loginpage import Login
from pages.dashboard import Dashboard
from pages.cart import CART
from pages.credential import Credentials
from pages.finishpage import Finish
from utilities import driver_setup
from utilities.driver_setup import get_driver

def test_test(driver):
    #login
    login = Login(driver)
    driver.get("https://www.saucedemo.com/")
    login.login()
    #dashboard
    dashboard=Dashboard(driver)
    dashboard.add()
    dashboard.gotocart()
    #cart
    cart=CART(driver)
    cart.checkout()
    #credentials
    cred=Credentials(driver)
    cred.credentials()
    cred.click_continue()
    #finish
    finish=Finish(driver)
    finish.finsh()

    assert "Thank you for your order!" in driver.page_source
    print("orderd using POM structure")