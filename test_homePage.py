import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomeScreen
from Utilities.BaseClass import BaseFixtureClass
from TestData.excelDemo import DataFromExcel

class TestHomePageEntries(BaseFixtureClass):

    def test_homeData(self, getData, setup):
        # Logging initialization
        log = self.getLogging(moduleName = __name__)

        # Initialize the HomeScreen page object
        home = HomeScreen(setup)

        # Interact with form fields and log the actions
        home.getName().send_keys(getData['name'])
        log.info(f"Name is {getData['name']}")

        home.getEmail().send_keys(getData['email'])
        log.info(f"Email is {getData['email']}")

        home.getPassword().send_keys(getData['password'])
        log.info(f"Password is {getData['password']}")

        # Interact with checkbox and dropdown
        home.checkbox().click()
        self.selectOption(home.dropDown(), getData['gender'])
        log.info(f"Gender is {getData['gender']}")

        # Wait for the submit button to be clickable
        WebDriverWait(setup, 10).until(EC.element_to_be_clickable(home.submit()))

        # Submit the form
        home.submit().click()

        # Capture and log the success message
        message = home.alertMessage().text
        log.info(f"Alert Message: {message}")

        # Refresh the page
        setup.refresh()

        # Assert success message is present
        assert "Success" in message

    @pytest.fixture(params=DataFromExcel().getTestData())
    def getData(self, request):
        # Return the parameterized test data from getTestData
        return request.param
