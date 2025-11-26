# Selenium Tutorial #2
# Perform a search and validate the results 

# Import required modules
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver 
driver = webdriver.Edge()

# Go to the website
driver.get("https://www.newgrounds.com")

# Wait for the search bar
try:
    topsearch = WebDriverWait(driver, 10).until (
        EC.presence_of_element_located((By.ID, "topsearch_text"))
    )
    # Perfom a search
    topsearch.send_keys("Linkin Park")
    time.sleep(1)
    topsearch.send_keys(Keys.RETURN)
except TimeoutException:
    print("Timeout")

# Wait for the page elements
try:
    results = WebDriverWait(driver, 10).until (
        EC.presence_of_element_located((By.XPATH, "//div[starts-with(@id, 'search_results_container_')]"))
    )
    # Validate Creations titles match search 
    print()
    print("/" * 8, "Creations", "/" * 8)
    print()
    itemlist1 = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'search_results_container_')]/ul[1]")
    for item in itemlist1:
        creations = item.find_elements(By.CLASS_NAME, "item-details")
        for creation in creations:
            titles = creation.find_elements(By.CLASS_NAME, "detail-title")
            for title in titles:
                print(title.text)
    # Validate Linkin and/or Park is in the text-content in the Community 
    print()
    print("/" * 8, "Community", "/" * 8)
    print()
    itemlist2 = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'search_results_container_')]/ul[2]")
    for item in itemlist2:
        posts = item.find_elements(By.CLASS_NAME, "searchitem-community-post")
        for post in posts:
            highlights = post.find_elements(By.CLASS_NAME, "search-highlight")
            for highlight in highlights:
                print(highlight.text)
    # Validate the number of Users
    print()
    print("/" * 8, "Users", "/" * 8)
    print()
    itemlist3 = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'search_results_container_')]/ul[3]") 
    for item in itemlist3:
        users = item.find_elements(By.CLASS_NAME, "item-user")
        if len(users) == 10:
            print("The number of users are: ", len(users))
        else:
            print("Error: missing users")
        print()    
except TimeoutException:
    print("Timeout")

# Exit the borwser
driver.quit()