from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class locationSection:

    loc = (By.ID, "country")
    countries_returned = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    terms_and_conditions = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.CLASS_NAME, "btn-success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a timeout of 10 seconds

    
    def address(self):
        self.driver.find_element(*locationSection.loc).send_keys("ind")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "suggestions")))  # Wait for the suggestions dropdown to appear

        # Loop through the suggestions to find and click "India"
        countries = self.driver.find_elements(*locationSection.countries_returned)
        for country in countries:
            if country.text == "India":  # Check if the suggestion text matches "India"
                country.click()  # Select "India" from the dropdown
                break

        # Select the terms and conditions checkbox
        self.driver.find_element(*locationSection.terms_and_conditions).click()

        # Click the "Purchase" button
        return self.driver.find_element(*locationSection.purchase_button)
        
