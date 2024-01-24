import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDrop:
    def drag_and_drop(self):
        ChromeDriverManager().install()
        chrome_option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        source = driver.find_element(By.XPATH, "//div[@id='draggable']")
        target = driver.find_element(By.XPATH, "//div[@id='droppable']")
        # driver is the web browser, and ActionChains(driver) is the set of instructions
        # for performing a drag-and-drop action with a specific offset on the web page
        # controlled by that driver.
        ActionChains(driver).drag_and_drop(source, target).perform()
        # ActionChains(driver).drag_and_drop_by_offset(source, 150, 35).perform()
        time.sleep(3)
        driver.quit()


dragAndDrop = DragAndDrop()
dragAndDrop.drag_and_drop()

