import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class EnableOrDisable:
    def enable_or_disable(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://training.openspan.com/login")
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("Prabha")
        # driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("12345")
        btnStatus = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        # if the action btn status is true then it is enabled,
        # else it is disabled
        print(btnStatus)
        time.sleep(3)


enableOrDisable = EnableOrDisable()
enableOrDisable.enable_or_disable()

