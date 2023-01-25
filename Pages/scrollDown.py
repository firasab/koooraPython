import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ScrollDown:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------
    def kooora_scroll_down(self, browser):
        time.sleep(10)
        try:
            htmlelement = self.browser.find_element(By.TAG_NAME, "html")
            htmlelement.send_keys(Keys.END)
            time.sleep(10)
            browser.save_screenshot("scrollDown.png")
        except:
            print("there is a problem with scroll down the page")
