import time
from selenium.webdriver.common.by import By


class DeleteAdv:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------
    def kooora_delete_adv(self):
        time.sleep(10)
        try:
            adv = self.browser.find_element(By.XPATH, "//*[@id=\"dismiss-button\"]")
            adv.click()
        except:
            print("there is a problem with the adv")