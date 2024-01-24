import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElementByLinkText:
    def locate_by_link_text(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
        time.sleep(3)

    def locate_by_partial_text(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs").click()
        time.sleep(3)


findByLinkTextOrPartialText = FindElementByLinkText()
# findByLinkTextOrPartialText.locate_by_link_text()
findByLinkTextOrPartialText.locate_by_partial_text()
