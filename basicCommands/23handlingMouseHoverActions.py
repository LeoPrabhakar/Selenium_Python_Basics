import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Used for waiting for a certain condition before proceeding with the execution.
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# Used for performing complex mouse and keyboard actions.
from selenium.webdriver.common.action_chains import ActionChains
# A set of predefined conditions that can be used with WebDriverWait to wait for specific conditions to be met.
from selenium.webdriver.support import expected_conditions as EC


class MouseHoverActions:
    def mouse_hover_actions(self):
        # Install ChromeDriver
        ChromeDriverManager().install()
        # Set up Chrome options and create a WebDriver instance
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        # Navigate to the Yatra website and maximize the window
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # Find the 'more' button element using its XPath
        moreBtn = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        # Create an instance of ActionChains to perform mouse actions
        a_chains = ActionChains(driver)
        # Perform the hover action using JavaScript
        # driver.execute_script("arguments[0].scrollIntoView(true);", moreBtn)
        # Move the mouse to the 'more' button and perform hover action
        a_chains.move_to_element(moreBtn).perform()
        # Set up WebDriverWait with a timeout of 10 seconds
        wait = WebDriverWait(driver, 10)
        # Wait for the 'booking_engine_trains' link to be clickable
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Luxury Trains']")))
        # Click on the link
        element.click()
        # An alternative way to click the element without using WebDriverWait (commented out)
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//a[@id='booking_engine_trains']").click()
        # Pause execution for 3 seconds (not recommended, consider using WebDriverWait)
        time.sleep(3)
        # Quit the WebDriver to close the browser window
        driver.quit()


# Create an instance of the MouseHoverActions class and execute the mouse_hover_actions method
mouseHoverActions = MouseHoverActions()
mouseHoverActions.mouse_hover_actions()

