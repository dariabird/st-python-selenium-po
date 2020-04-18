from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    HOME_LOCATOR = By.CSS_SELECTOR, 'i[title=Home]'
    CART_LOCATOR = By.XPATH, '//a[contains(., "Checkout")]'
    CART_COUNTER_LOCATOR = By.CSS_SELECTOR, 'a.content'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def home(self):
        return self.driver.find_element(*self.HOME_LOCATOR)

    @property
    def cart(self):
        return self.driver.find_element(*self.CART_LOCATOR)

    def go_home(self):
        self.home.click()

    def go_to_cart(self):
        self.cart.click()

    def is_element_present(self, *args):
        try:
            self.driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False

    def are_elements_present(self, *args):
        return len(self.driver.find_elements(*args)) > 0

    def wait_for_element_present(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def wait_for_elements_present(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return None
