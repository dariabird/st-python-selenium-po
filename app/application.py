from selenium import webdriver
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.start_page import StartPage
from pages.product_page import ProductPage


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.start_page = StartPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_product_to_cart(self):
        self.start_page.open()
        self.start_page.open_first_product_page()
        self.product_page.add_product_to_cart()
        # self.base_page.go_home()

    def delete_product_from_cart(self):
        self.cart_page.open()
        self.cart_page.remove_product_from_cart()
