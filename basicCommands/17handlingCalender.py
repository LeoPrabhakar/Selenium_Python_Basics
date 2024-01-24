import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class HandlingAutoSuggestion:
    def auto_suggestion(self):
        ChromeDriverManager().install()
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get("https://www.yatra.com/flights")
            driver.maximize_window()

            depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
            depart_from.click()
            time.sleep(2)
            depart_from.send_keys("New Delhi")
            time.sleep(2)
            depart_from.send_keys(Keys.ENTER)
            time.sleep(3)

            going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
            going_to.click()
            time.sleep(2)
            going_to.send_keys("New")
            time.sleep(2)

            search_list = driver.find_elements(By.XPATH, "//div[@class='viewport']//div/li")
            for result in search_list:
                if "New York (NYC)" in result.text:
                    result.click()
                    break
            time.sleep(3)

            origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
            origin.click()
            time.sleep(4)

            all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//tr/td[@class!='inActiveTD']")
            for date in all_dates:
                if date.get_attribute("date-date") == "15/01/2024":
                    date.click()
                    time.sleep(3)
                    break
        finally:
            driver.quit()


auto_suggestion = HandlingAutoSuggestion()
auto_suggestion.auto_suggestion()
