import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ImplicitWait:
    def implicit_wait(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        # If the element is not immediately found, WebDriver will wait up to 5 seconds
        # for the element to appear in the DOM before raising a "NoSuchElementException".
        # The implicit wait is applied to all find_element* and find_elements* methods.
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password123']").send_keys("secret_sauce")
        time.sleep(3)
        driver.quit()


implicitWait = ImplicitWait()
implicitWait.implicit_wait()

