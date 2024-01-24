import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HandlingAlerts:
    def handling_alert(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Alert']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.quit()
        print("----------------------------------------------------------------------")

    def handling_confirm_box(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        # driver.switch_to.alert.accept()
        driver.switch_to.alert.dismiss()
        getText = driver.find_element(By.XPATH, "//p[@id='demo']").text
        print(getText)
        time.sleep(3)
        driver.quit()
        print("----------------------------------------------------------------------")


    def handling_prompt_alert(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Prompt']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Leo")
        # driver.switch_to.alert.send_keys("")
        driver.switch_to.alert.accept()
        # driver.switch_to.alert.dismiss()
        getText = driver.find_element(By.XPATH, "//p[@id='demo']").text
        print(getText)
        time.sleep(2)
        driver.quit()


handlingAlert = HandlingAlerts()
# handlingAlert.handling_alert()
# handlingAlert.handling_confirm_box()
handlingAlert.handling_prompt_alert()

