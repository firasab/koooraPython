class LoadPage:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
#----------------------------------------------------------------------------------
    def load(self):
        try:
            self.browser.get("https://www.kooora.com/")
        except:
            print("there is a problem with the website")

        try:
            self.browser.maximize_window()

        except:
            print("we cant max the window")
#----------------------------------------------------------------------------------
