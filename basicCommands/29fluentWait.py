import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FluentWait:
    def fluent_wait(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        fluent_wait = WebDriverWait(driver, 5, 2, ignored_exceptions=[TimeoutException])
        # fluent_wait.ignored_exceptions = [TimeoutException]
        fluent_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        # time.sleep(3)
        driver.quit()


fluentWait = FluentWait()
fluentWait.fluent_wait()
