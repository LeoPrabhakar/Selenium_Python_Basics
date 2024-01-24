import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver.current_url
# driver.back
# driver.forward
# driver.refresh
# driver.title
# driver.maximize_window
# driver.minimize_window
# driver.fullscreen.window
# driver.close
# driver.quit


class AllBrowserMethods:
    def browser_methods(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.saucedemo.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        # driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)

allBrowserMethods = AllBrowserMethods()
allBrowserMethods.browser_methods()

