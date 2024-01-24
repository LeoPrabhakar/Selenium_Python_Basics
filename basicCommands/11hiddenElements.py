import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HiddenElements:
    # Approach 1:- element is still there in the DOM once hide button is clicked
    def Aprch1_hidden_elements(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        hiddenElementStatusBefore = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        hiddenElementStatusAfter = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(hiddenElementStatusBefore)
        print(hiddenElementStatusAfter)
        driver.quit()

    # Approach 2:- element is completely gone from the DOM once button is clicked
    def Aprch2_hidden_elements(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        hiddenStatus1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(hiddenStatus1)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        hiddenStatus2 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(hiddenStatus2)
        driver.quit()


hiddenElements = HiddenElements()
# hiddenElements.Aprch1_hidden_elements()
hiddenElements.Aprch2_hidden_elements()


# 2nd approach will give an error
# raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: