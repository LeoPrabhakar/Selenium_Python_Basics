import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HandlingMutipleWindows:
    def multiple_windows(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # Retrieves and prints the handle (identifier) of the current window (parent window).
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        # Retrieves and prints the handles of all open windows after the new window is opened.
        all_handle1 = driver.window_handles
        print(all_handle1)
        # Iterates through the window handles and switches to the newly opened window.
        for handle in all_handle1:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                # Clicks on an element with the link text "Terms of Service" in the new window.
                driver.find_element(By.LINK_TEXT, "Terms of Service").click()
                # Retrieves and prints the handles of all open windows again (including the new one)
                all_handle2 = driver.window_handles
                print(all_handle2)
                time.sleep(3)
                #  Breaks out of the loop after handling the first new window.
                driver.close()
                time.sleep(3)
                # Break out of the loop after handling the first new window break
                break

        # Switches back to the parent window using the parent window handle.
        driver.switch_to.window(parent_handle)
        time.sleep(3)
        # Clicks on the same element in the parent window to open another new window.
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        time.sleep(3)


# Creates an instance of the HandlingMutipleWindows class
# and calls the multiple_windows method to execute the defined actions.
handlingMultipleWindows = HandlingMutipleWindows()
handlingMultipleWindows.multiple_windows()

