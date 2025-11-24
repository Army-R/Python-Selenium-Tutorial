# Selenium Tutorial #1
# Validate the title of the website

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Set variables
title = "Newgrounds.com — Everything, By Everyone"

# Path to the EdgDriver 
PATH = r"path\msedgedriver.exe"

# Create a service object
service = Service(executable_path=PATH)

# Initialize the EdgDriver with the service
driver = webdriver.Edge(service=service)

# Open the website
driver.get("https://newgrounds.com")

# Validate the title
if driver.title == title:
    print("Title is correct")
    driver.quit()
else:
    print("Title does not match, current title is: ", driver.title)