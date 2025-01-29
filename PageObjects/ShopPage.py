from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutSection

class ShopSection:
    all_mobiles = (By.XPATH, "//div[@class='card h-100']")
    each_mobile_name = (By.CSS_SELECTOR, "h4[class*='card-title']")
    req_mobile = (By.CSS_SELECTOR, "button[class*='btn btn-info']")
    checkout_button = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def mobileCheckout(self):
        # Locate all product cards on the shop page
        mobiles = self.driver.find_elements(*ShopSection.all_mobiles)

        # Loop through all product cards to find a specific mobile
        for mobile in mobiles:
            mobile_name = mobile.find_element(*ShopSection.each_mobile_name).text  # Extract the product name
            if mobile_name == "Blackberry":  # Check if the product name matches "Blackberry"
                mobile.find_element(*ShopSection.req_mobile).click()  # Click the "Add to cart" button
                break  # Stop searching once the desired mobile is found

        # Click on the "Checkout" button in the navigation bar
        self.driver.find_element(*ShopSection.checkout_button).click()
        return CheckoutSection(self.driver)
