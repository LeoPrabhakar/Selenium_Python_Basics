import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class HanldingMultiSelection():
    def multi_selection(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        dropdown = driver.find_element(By.XPATH, "//select[@id='colors']")
        dd = Select(dropdown)
        dd.select_by_index(0)
        time.sleep(2)
        dd.select_by_value("blue")
        time.sleep(2)
        dd.select_by_visible_text("Green")
        time.sleep(2)
        # dd.deselect_by_index(0)
        # time.sleep(2)
        # dd.deselect_by_value("blue")
        # time.sleep(2)
        # dd.deselect_by_visible_text("Green")
        # time.sleep(2)
        dd.deselect_all()
        driver.quit()

handlingMultiSelection = HanldingMultiSelection()
handlingMultiSelection.multi_selection()
