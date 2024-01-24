import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElementByCSS:
    def locate_by_css(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        elementSS = driver.find_element(By.CSS_SELECTOR, "#login-button")
        elementSS.screenshot("C:\\browserDrivers\\Screenshots\\loginBtn.png")
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\browserDrivers\\Screenshots\\wholePage1.png")
        driver.save_screenshot("C:\\browserDrivers\\Screenshots\\wholePage2.png")


findByCSS = FindElementByCSS()
findByCSS.locate_by_css()

