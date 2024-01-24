import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class handlingAutoSuggestion():
    def auto_suggestion(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.yatra.com/flights")
        departFrom = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departFrom.click()
        time.sleep(2)
        departFrom.send_keys("New Delhi")
        time.sleep(2)
        departFrom.send_keys(Keys.ENTER)
        time.sleep(3)
        goingTo = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        goingTo.click()
        time.sleep(2)
        goingTo.send_keys("New")
        time.sleep(2)
        # note:- if it is multiple elements to iterate use "find_elements" instead "find_element"
        search_list = driver.find_elements(By.XPATH, "//div[@class='viewport']//div/li")
        for results in search_list:
            if "New York (NYC)" in results.text:
                results.click()
                break
        time.sleep(3)
        driver.quit()


autoSuggestion = handlingAutoSuggestion()
autoSuggestion.auto_suggestion()

