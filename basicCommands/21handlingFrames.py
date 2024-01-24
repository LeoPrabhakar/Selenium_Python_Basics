import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HandlingFrames:
    def handling_frames(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        # switch with locator
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        # switch with id
        # driver.switch_to.frame("iframeResult")
        # switch with name
        driver.switch_to.frame("iframeResult")
        # switch with 0th index
        driver.switch_to.frame(0)
        searchBox = driver.find_element(By.XPATH, "//a[@title='SQL Tutorial'][normalize-space()='SQL']")
        time.sleep(3)
        searchBox.click()
        time.sleep(3)


handlingFrames = HandlingFrames()
handlingFrames.handling_frames()