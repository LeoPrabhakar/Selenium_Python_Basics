# time: Provides various time-related functions.
import time
# webdriver from Selenium: Allows interaction with a web browser.
from selenium import webdriver
# By from selenium.webdriver.common.by: Provides mechanisms for locating elements on a web page.
from selenium.webdriver.common.by import By
# ChromeDriverManager from webdriver_manager.chrome: Manages the installation and configuration of the ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  Installs ChromeDriver using ChromeDriverManager and sets up the Chrome browser.
ChromeDriverManager().install()
chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
# Wait for an element to be present on the next page (adjust the timeout as needed)
wait = WebDriverWait(driver, 10)
product_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
# Assertion to check if the product label is displayed on the page
assert product_title.is_displayed(), "Login failed, product label not found on the page"
# Add an optional sleep to see the result (you may remove this in a real test scenario)
time.sleep(5)
driver.quit()
