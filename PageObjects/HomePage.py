from selenium.webdriver.common.by import By
from PageObjects.ShopPage import ShopSection

class HomeScreen:
    name = "name"
    email = "email"
    password_id = "exampleInputPassword1"
    checkbox_css = "input[type=checkbox]"
    dropDown_id = "exampleFormControlSelect1"
    gender_vText = "Male"
    submit_path = "//input[@type='submit']"
    alert_message_class = "alert-success"
    password_id = "exampleInputPassword1"

    def __init__(self, driver):
        self.driver = driver
        self.shop_element = By.CSS_SELECTOR
        self.shop_value = "a[href*='shop']"
    def clickShop(self):
        self.driver.find_element(self.shop_element, self.shop_value).click()
        return ShopSection(self.driver)
    def getName(self):
        return self.driver.find_element(By.NAME, self.name)
    def getEmail(self):
        return self.driver.find_element(By.NAME, self.email)
    def getPassword(self):
        return self.driver.find_element(By.ID, self.password_id)
    def checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.checkbox_css)
    def dropDown(self):
        return self.driver.find_element(By.ID, self.dropDown_id)
    def submit(self):
        return self.driver.find_element(By.XPATH, self.submit_path)
    def alertMessage(self):
        return self.driver.find_element(By.CLASS_NAME, self.alert_message_class)