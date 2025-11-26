# Selenium Tutorial #1
# Validate the title of the website

# Import webdriver module
from selenium import webdriver

# Set variables
title = "Newgrounds.com — Everything, By Everyone"

# Initialize the EdgDriver
driver = webdriver.Edge()

# Open the website
driver.get("https://newgrounds.com")

# Validate the title
if driver.title == title:
    print("Title is correct")
else:
    print("Title does not match, current title is: ", driver.title)

# Exit the browser
driver.quit()