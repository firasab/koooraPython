import time
from selenium.webdriver.common.by import By


class GetInfo:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------
    def kooora_games_get_information(self):
        time.sleep(10)
        try:
            English_Premier_League_best_Player = self.browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div[3]/table/tbody/tr[1]")
            information = English_Premier_League_best_Player.text
            print(information)
            enter_to_the_list = self.browser.find_element(By.LINK_TEXT, "قائمة الهدافين")
            enter_to_the_list.click()


        except:
            print("we cant get that element")
#----------------------------------------------------------------------------------