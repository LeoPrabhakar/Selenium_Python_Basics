import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RightAndDoubleCLick:
    def right_click(self):
        # Install ChromeDriver
        ChromeDriverManager().install()
        # Set up Chrome options and create a WebDriver instance
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        # Navigate to the Yatra website and maximize the window
        driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        driver.maximize_window()
        a_chains = ActionChains(driver)
        element = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        a_chains.context_click(element).perform()
        time.sleep(3)
        driver.quit()

    def double_click(self):
        # Install ChromeDriver
        ChromeDriverManager().install()
        # Set up Chrome options and create a WebDriver instance
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        # Navigate to the Yatra website and maximize the window
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        action_chains = ActionChains(driver)
        field1_value = driver.find_element(By.XPATH, "//input[@id='field1']").get_attribute("value")
        print(field1_value)
        element = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
        action_chains.double_click(element).perform()
        try:
            field2_value = driver.find_element(By.XPATH, "//input[@id='field2']").get_attribute("value")
            if not field2_value:
                raise ValueError("The double-click button action has not been executed yet")
            print(field2_value)
        except Exception as e:
            print(f"Error getting text: {e}")
        time.sleep(3)
        driver.quit()


rightAndDoubleClick = RightAndDoubleCLick()
rightAndDoubleClick.right_click()
rightAndDoubleClick.double_click()

