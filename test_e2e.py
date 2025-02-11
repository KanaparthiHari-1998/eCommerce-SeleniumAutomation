from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomeScreen
from Utilities.BaseClass import BaseFixtureClass
# from test_homePage import TestHomePageEntries


class TestFirstProgramWithPytestAndSelenium(BaseFixtureClass):

    def test_e2e(self, setup):

        log = self.getLogging(moduleName = __name__)
        # Initialize WebDriverWait with a timeout of 10 seconds
        wait = WebDriverWait(setup, 10)
        # Step 1: Navigate to the shop page
        home = HomeScreen(setup)
        shop = home.clickShop()
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*='my-4']"))
        )  # Wait until the shop heading is visible

        # Step 2: Add a specific mobile to the cart and proceed to checkout
        shopPage = shop.mobileCheckout()
        checkoutPage = shopPage.checkout()
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div/a[contains(text(),'ProtoCommerce Home')]"))
        )  # Wait until the checkout page loads

        # Step 3: Place the order
        locationPage = checkoutPage.address()
        locationPage.click()

        # Step 4: Validate the success message
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success')]"))
        )  # Wait for the success message to appear
        log.info("Alert is activated")

        success_message = setup.find_element(
            By.XPATH, "//div[contains(@class, 'alert-success')]"
        ).text
        log.info(success_message)

        # Assert the success message contains the expected text
        assert "Success! Thank you!" in success_message