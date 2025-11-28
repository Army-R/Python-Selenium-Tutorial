#main.py

# Import necessary modules
import unittest # Import the unittest module for creating test cases
from selenium import webdriver
import page

# Create a test case class
class PythonOrgSearch(unittest.TestCase):

    # Set up method to initialize the WebDriver
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.python.org")
         
    # Test method to validate the title of the main page
    def test_title(self):
        main_page = page.MainPage(self.driver) 
        self.assertTrue(main_page.validate_tite()) 

    # Test method to click the go button
    def test_go_button(self):
        main_page = page.MainPage(self.driver) 
        self.assertTrue(main_page.click_go_button())

    # Clean up method to close the WebDriver
    def tearDown(self):
        self.driver.quit()


# Only run the tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()



