from selenium.webdriver.common.by import By
from PageObjects.LocationPage import locationSection

class CheckoutSection:
    checkout_button = (By.CSS_SELECTOR, "button[class*='btn btn-success']")
    def __init__(self, driver):
        self.driver = driver
    
    def checkout(self):
        self.driver.find_element(*CheckoutSection.checkout_button).click()
        return locationSection(self.driver)
