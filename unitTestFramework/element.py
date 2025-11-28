#element.py

# Import necessary modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Create a class that represent one element on the page
class BasePageElement(object):
    # Function to set a value for any element on the web page
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.NAME, self.locator) # Wait until the element is found
        )
        driver.find_element(By.NAME, self.locator).clear() # Find the element locator and clear it 
        driver.find_element(By.NAME, self.locator).send_keys(value) # Send the value to the element
    
    # Function to get the value of any element on the web page
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.NAME, self.locator) 
        )
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")
