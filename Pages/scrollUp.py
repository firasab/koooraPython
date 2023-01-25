import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ScrollUp:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------
    def kooora_scroll_up(self, browser):
        time.sleep(10)
        try:
            htmlelement = self.browser.find_element(By.TAG_NAME, "html")
            htmlelement.send_keys(Keys.HOME)
            time.sleep(10)
            browser.save_screenshot("scrollUp.png")
        except:
            print("There is a problem with scroll up the page")
