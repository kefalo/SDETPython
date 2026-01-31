import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to the ChromeDriver executable
chrome_driver_path = r'C:\chromedriver-win64\chromedriver.exe'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome driver with the service
driver = webdriver.Chrome(service=service)

# Open Google
driver.get('http://www.onlyfans.com/')
time.sleep(5)  # Let the user actually see something

# Find the search box and perform a search
emailLocator = driver.find_element(By.NAME, "email")
passField = driver.find_element(By.NAME, "password")
emailLocator.click()
emailLocator.send_keys("stefan@test.com")
passField.click()
passField.send_keys("govnoSelenium")

# emailLocator.submit()
time.sleep(30)# Let the user actually see something

# Close the browser
driver.quit()
