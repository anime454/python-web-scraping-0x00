from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

# Set up options to enable headless mode
options = Options()
options.add_argument("--headless")

# Initialize the Chrome WebDriver with the configured options
driver = webdriver.Chrome(options=options)

# Navigate to the historical trading page for PTT on SetTrade
driver.get("https://www.settrade.com/th/equities/quote/ptt/historical-trading")

# Wait for 1 second to allow all page elements to finish loading.
time.sleep(1)

# Simulate pressing the END key to scroll to the bottom of the page.
# This is important to ensure that all elements, including the table, are loaded.
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)

# Wait for 2 seconds to ensure that the data in the table finishes loading.
time.sleep(2)

# Get the table element using its ID ('historical-table').
element = driver.find_element(By.ID, "historical-table")

# Print the inner HTML content of the table element.
print("HTML content of the historical table:")
print(element.get_attribute('innerHTML'))

# If you want to retrieve the text content of the table, use the following line.
# print("Text content of the historical table:")
# print(element.text)

# Close the WebDriver session.
driver.quit()
