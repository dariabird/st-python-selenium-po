import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_SHORTCUTS_LOCATOR = By.CSS_SELECTOR, 'ul.shortcuts li'
    PRODUCT_SHORTCUT = By.CSS_SELECTOR, 'ul.shortcuts li a'
    ORDER_SUMMARY_LOCATOR = By.ID, 'box-checkout-summary'
    REMOVE_BUTTON_LOCATOR = By.CSS_SELECTOR, 'button[name="remove_cart_item"]'

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        return self

    @property
    def product_shortcut(self):
        return self.driver.find_element(*self.PRODUCT_SHORTCUT)

    @property
    def remove_button(self):
        return self.driver.find_element(*self.REMOVE_BUTTON_LOCATOR)

    @property
    def order_summary(self):
        return self.driver.find_element(*self.ORDER_SUMMARY_LOCATOR)

    def remove_product_from_cart(self):
        if self.are_elements_present(*self.PRODUCT_SHORTCUTS_LOCATOR):
            time.sleep(1)
            self.product_shortcut.click()
        if self.is_element_present(*self.REMOVE_BUTTON_LOCATOR):
            order_summary = self.order_summary
            self.remove_button.click()
            self.wait.until(EC.staleness_of(order_summary))
