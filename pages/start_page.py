import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):
    PRODUCTS_LOCATOR = By.CSS_SELECTOR, 'ul.products li'

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    @property
    def products(self):
        return self.driver.find_elements(*self.PRODUCTS_LOCATOR)

    def open_first_product_page(self):
        time.sleep(1)
        self.products[0].click()
