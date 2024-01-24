import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWait:
    def explicit_wait(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        # Unlike implicit waits, which are applied globally to all elements,
        # explicit waits are used for specific elements or conditions.
        # With explicit waits, you can instruct the WebDriver to wait for a certain condition
        # to be met before proceeding with the execution of the next steps.
        explicit_wait = WebDriverWait(driver, 5)
        explicit_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button123']"))).click()
        # driver.find_element(By.XPATH, "//input[@id='login-button123']").click()
        # time.sleep(3)
        driver.quit()


explicitWait = ExplicitWait()
explicitWait.explicit_wait()

