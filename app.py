# Python program to demonstrate automation using selenium. This script will automate searching Amazon for "Raspberry Pi 4" best pricing. 
# 
# selenium 
  
# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create webdriver object 
driver = webdriver.Chrome() 
# get website
driver.get("https://amazon.com")
# print(driver.title)

search = driver.find_element_by_name("field-keywords")
search.send_keys("Raspberry Pi 4")
search.send_keys(Keys.RETURN)

# Explicit Waits
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
    

main = driver.find_element_by_id("main")
print(main.text)

#driver.close()


