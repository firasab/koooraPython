from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GO_TO_THE_PAGE:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
#----------------------------------------------------------------------------------
    def go_to_The_page(self, title):
        time.sleep(10)
        try:
            page_title = self.browser.find_element(By.LINK_TEXT, title)
        except:
            print(f'there is a problem with going to this page {title}')

        page_title.click()
        time.sleep(10)
#----------------------------------------------------------------------------------

