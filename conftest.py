import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add command-line option for browser selection
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

# Define a fixture to set up the Selenium WebDriver
@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    

    # Configure the WebDriver based on the selected browser
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        # options = webdriver.FirefoxOptions()
        # options.add_argument("headless")  # Uncomment if headless mode is required
        driver = webdriver.Firefox()
    elif browser == "IE":
        # options = webdriver.IeOptions()
        # options.add_argument("headless")  # Uncomment if headless mode is required
        driver = webdriver.Ie() 
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Set up WebDriverWait and open the target URL
    wait = WebDriverWait(driver, 10)
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='form-group']/input[@name='name']")))
    driver.maximize_window()

    # Attach the WebDriver instance to the test class
    request.cls.driver = driver

    # Yield the driver to the tests
    yield driver


    # Quit the WebDriver after the test execution
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Capture screenshot on failed tests and add it to HTML report """
    if call.when == 'call' and call.excinfo is not None:
        # Capture screenshot on failure
        screenshot_path = item.instance.capture_screenshot(item.name)
        
        # Attach screenshot to HTML report if pytest-html is used
        if "html" in item.config.pluginmanager.get_plugins():
            # Add the screenshot path to the extra information of the test item
            extra = getattr(item, 'extra', [])
            extra.append(pytest_html.extras.image(screenshot_path))
            item.extra = extra
