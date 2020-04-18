class is_text_of_element_changed(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = driver.find_element(*self.locator).text
        return actual_text != self.text
