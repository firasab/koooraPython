class CheckTittle:
#----------------------------------------------------------------------------------
    def __init__(self, browser):
        self.browser = browser
# #----------------------------------------------------------------------------------

    def kooora_check_tittle(self, title):
        website_title = self.browser.title
        try:
            assert website_title == title
        except:
            print("we are not in the right tittle")
# ----------------------------------------------------------------------------------