from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.helper import is_text_of_element_changed


class ProductPage(BasePage):
    SIZE_SELECTOR_LOCATOR = By.CSS_SELECTOR, 'select[name="options[Size]"]'
    ADD_TO_CART_BUTTON_LOCATOR = By.NAME, "add_cart_product"

    @property
    def size_selector(self):
        return Select(self.driver.find_element(*self.SIZE_SELECTOR_LOCATOR))

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(*self.ADD_TO_CART_BUTTON_LOCATOR)

    def select_product_size(self, index=1):
        self.size_selector.select_by_index(index)

    def add_product_to_cart(self):
        self.wait_for_element_present(self.ADD_TO_CART_BUTTON_LOCATOR)
        if self.is_element_present(*self.SIZE_SELECTOR_LOCATOR):
            self.select_product_size()
        cart_counter_text = self.driver.find_element(*self.CART_COUNTER_LOCATOR).text
        self.add_to_cart_button.click()
        self.wait.until(is_text_of_element_changed(self.CART_COUNTER_LOCATOR, cart_counter_text))

