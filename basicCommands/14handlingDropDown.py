import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class HanldingDropDown():
    def drop_down(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        dropdown = driver.find_element(By.XPATH, "//select[@id='country']")
        dd = Select(dropdown)
        dd.select_by_index(1)
        time.sleep(2)
        dd.select_by_value("germany")
        time.sleep(2)
        dd.select_by_visible_text("India")
        time.sleep(2)
        driver.quit()

handlingDropDown = HanldingDropDown()
handlingDropDown.drop_down()
