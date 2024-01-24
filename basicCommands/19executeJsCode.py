import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class BasicJS:
    def basic_js(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        #driver.get("https://www.saucedemo.com/")
        driver.execute_script("window.open('https://www.saucedemo.com/','_self');")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(2)
        sauceP1 = driver.execute_script("return document.getElementsByTagName('a')[6];")
        driver.execute_script("arguments[0].click();", sauceP1)
        time.sleep(3)
        driver.quit()

basicJS = BasicJS()
basicJS.basic_js()

