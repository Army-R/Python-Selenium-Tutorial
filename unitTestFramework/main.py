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

    # Test method to type, search and validate the results
    def test_search(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = main_page.search_word # Search for "pycon"
        main_page.click_go_button() # Click the go button
        self.assertTrue(main_page.click_go_button()) # Validate URL change
        search_results_page = page.SearchResultsPage(self.driver)
        self.assertTrue(search_results_page.validate_results()) # Validate that results are found

    # Clean up method to close the WebDriver
    def tearDown(self):
        self.driver.quit()

# Only run the tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()