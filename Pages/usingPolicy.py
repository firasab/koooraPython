import time
from selenium.webdriver.common.by import By


class UsingPolicy:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------
    def kooora_using_policy(self):
        time.sleep(10)
        try:
            using_policy = self.browser.find_element(By.LINK_TEXT, "سياسة الاستخدام")
            using_policy.click()
            time.sleep(10)
        except:
            print("there is problem with the linked text")
