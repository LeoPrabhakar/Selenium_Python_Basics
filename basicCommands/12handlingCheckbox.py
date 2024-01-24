import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HanldingCheckBox():
    def check_box(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, "#sunday").click()
        time.sleep(3)
        radioBtnSatus1 = driver.find_element(By.CSS_SELECTOR, "#sunday").is_selected()
        print(radioBtnSatus1)
        driver.find_element(By.CSS_SELECTOR, "#sunday").click()
        time.sleep(3)
        radioBtnSatus2 = driver.find_element(By.CSS_SELECTOR, "#sunday").is_selected()
        print(radioBtnSatus2)
        driver.quit()
        time.sleep(3)

handlingCheckBox = HanldingCheckBox()
handlingCheckBox.check_box()

