import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElementByTagName:
    def locate_by_tag_name(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.CLASS_NAME, "input_error form_input").send_keys("standard_user")
        time.sleep(3)

    def locate_by_class_name(self):
        # Install the Chrome driver using ChromeDriverManager
        ChromeDriverManager().install()
        # Set options separately
        chrome_options = webdriver.ChromeOptions()
        # Add any options you need, such as headless mode or others
        # Initialize the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.TAG_NAME,"input").send_keys("standard_user")
        time.sleep(3)


findByTagOrClassName= FindElementByTagName()
findByTagOrClassName.locate_by_tag_name()
findByTagOrClassName.locate_by_class_name()

