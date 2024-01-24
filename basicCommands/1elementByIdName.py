# note:----------------
# driver = webdriver.Chrome(options=chrome_options)
# The webdriver.ChromeOptions() class in Selenium is used to customize
# and configure the behavior of the Chrome browser when controlled through the WebDriver.
# It allows you to set various options and preferences for the browser session.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElementByIdName:
    def locate_by_id(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    def locate_by_name(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        time.sleep(3)


findByIdName = FindElementByIdName()
# findByIdName.locate_by_id()
findByIdName.locate_by_name()

