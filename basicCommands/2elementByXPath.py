import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FindElementByXPath:
    def locate_by_xpath(self):
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
        time.sleep(3)

findByXPath = FindElementByXPath()
findByXPath.locate_by_xpath()

