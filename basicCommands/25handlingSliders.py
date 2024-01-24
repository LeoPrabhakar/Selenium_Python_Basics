# By using a try-finally block, you make sure that resources are properly cleaned up,
# and the WebDriver is closed gracefully, enhancing the robustness of your script.
# If an exception occurs, the 'finally' block will still be executed before the exception is propagated,
# allowing you to perform cleanup operations.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class HandlingSliders:
    def handling_sliders(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        # A try block is used to encapsulate the slider handling logic,
        try:
            driver.get("https://www.snapdeal.com/search?keyword=mobiles&sort=rlvncy")
            driver.maximize_window()
            element1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
            element2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
            # approach 1
            # ActionChains(driver).drag_and_drop_by_offset(element1, 60, 0).perform()
            # approach 2
            # ActionChains(driver).click_and_hold(element1).pause(1).move_by_offset(60, 0).release().perform()
            # approach 3
            ActionChains(driver).move_to_element(element1).click_and_hold(element1).pause(1)\
                .move_by_offset(60, 0).release().perform()
            time.sleep(5)
            ActionChains(driver).drag_and_drop_by_offset(element2, -60, 0).perform()
            time.sleep(3)
        # 'finally' block ensures that the browser is closed (driver.quit())
        # even if an exception occurs during execution.
        finally:
            driver.quit()


handlingSliders = HandlingSliders()
handlingSliders.handling_sliders()

