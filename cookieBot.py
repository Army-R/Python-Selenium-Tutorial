# Selenium Tutorial 4
# Cookie bot

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

# Initialize Edge driver
driver = webdriver.Edge()

try:
    # Open a webpage
    driver.get("https://cookieclicker.ee/")

    # Wait for the language selection element to be clickable and select English
    try:
        language = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "langSelect-EN"))
        )
        language.click()
    finally:
        driver.implicitly_wait(3)

    # Set variables for elements
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element
            (By.ID, "product" + str(i)) 
            for i in range(1, -1, -1)
            ]

    # Create an instance of ActionChains
    actions = AC(driver)

    # Perform cookie clicking and item purchasing
    for i in range(500):
        actions.click(cookie).perform()
        count = int(cookie_count.text.split()[0]) # Get current cookie count
    
        for item in items:
            try:
                price = int(item.text.split()[1])
                
                if price <= count:
                    actions.move_to_element(item).click().perform()
            except:
                continue # Skip if item is not purchasable yet

        # Break the loop after reaching 30 cookies        
        if count >= 30:
            break

finally:
    # Close the browser
    driver.quit()    