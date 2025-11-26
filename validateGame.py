# Selenium Tutorial #3
# Start a game and go back to main page

# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# Go to the website
driver.get("https://www.newgrounds.com")

# Wait for the "Games" link to be present and click it
try:
    games = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Games"))
    )
    # Click on the "Games" link
    games.click()
    # Wait for the game card to load
    try:
        shoot = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='TRY SHOOT ME' and @class='inline-card-portalsubmission']"))
        )
        # Click on the game card
        shoot.click()
        # Wait for play game button to load
        try:
            play = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "barrier_close_btn"))
            )
            # Click on play game button
            play.click()
            # Wait for the game load
            time.sleep(15)           
            # Go back to the main page
            driver.back()
            driver.back()
            # Wait for Games link before closing
            try:
                games = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Games"))
            )
                print("Test completed successfully")    
            except TimeoutException:
                print("Did not return to Main page")    
        except TimeoutException:
            print("Game did not start")
    except TimeoutException:
        print("Game card not found")
except TimeoutException:
    print("Timeout")

# Close the browser
driver.quit()
