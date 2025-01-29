from datetime import datetime
import logging
import os
import pytest
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseFixtureClass:
    def selectOption(self, locator, text):
        dropInfo = Select(locator)
        dropInfo.select_by_visible_text(text)
    
    def getLogging(self, moduleName = None):
        logger = logging.getLogger(moduleName if moduleName else __name__)
        if not logger.handlers:
            fileHandler = logging.FileHandler("TestLogging.log")
            logger.addHandler(fileHandler)
            log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            fileHandler.setFormatter(log_format)
            logger.setLevel(logging.DEBUG)    
        return logger
    
    def capture_screenshot(self, test_name):
        """Captures a screenshot and saves it with the test name and timestamp."""
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path