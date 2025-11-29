#page.py

# Import necessary modules
from locator import MainPageLocators
from element import BasePageElement
import re

# Define a class to interact with the search bar element
class SearchTextElement(BasePageElement):
    locator = "q"  

# Define the base class for all of our pages
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver # Pass the driver

# Define a class for each page we're going to test

class MainPage(BasePage):
    # Define the search text element
    search_text_element = SearchTextElement()
    # Define the word to be searched
    search_word = "pycon"
    # Method to validate the title of the main page
    def validate_tite(self):
        return "Python" in self.driver.title
    # Method to click on go button
    def click_go_button(self):
        go_button = self.driver.find_element(*MainPageLocators.GO_BUTTON) # Unpack the locator tuple with *, so there are two arguments
        go_button.click()
        # Validate URL change after clicking the button
        current_url = self.driver.current_url
        return re.search(rf"/search/\?q={self.search_word}&submit=", current_url) # Regex to match expected URL pattern
            
class SearchResultsPage(BasePage):
    def validate_results(self):
        return "No results found." not in self.driver.page_source 