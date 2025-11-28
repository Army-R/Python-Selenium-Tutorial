#page.py

# Import necessary modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import MainPageLocators
import re

# Define the base class for all of our pages
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver # Pass the driver

# Define a class for each page we're going to test

class MainPage(BasePage):

    # Method to validate the title of the main page
    def validate_tite(self):
        return "Python" in self.driver.title
    
    # Method to click on go button
    def click_go_button(self):
        try:
            go_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.GO_BUTTON)  
            )
            go_button.click()
            # Validate URL change after clicking the button
            current_url = self.driver.current_url
            return re.search(r"/search/\?q=&submit=", current_url) # Regex to match expected URL pattern
        except:
            return False