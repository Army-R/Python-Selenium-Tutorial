#locator.py
# Define locators for web elements

# Import necessary module
from selenium.webdriver.common.by import By

# Class to define all locators for the Main Page
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit") # Capitalized to indicate constants