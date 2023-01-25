from selenium import webdriver
from Pages.checkTittle import CheckTittle
from Pages.getInfo import GetInfo
from Pages.goTo import GO_TO_THE_PAGE
from Pages.loadPage import LoadPage
from Pages.scrollDown import ScrollDown
from Pages.scrollUp import ScrollUp
from Pages.usingPolicy import UsingPolicy

def test_function():
# -----------------------------------------------------------------
    # create a new Chrome browser instance
    browser = webdriver.Chrome("chromedriver.exe")
#-----------------------------------------------------------------
    # get load function from LoadPage page
    load_Website = LoadPage(browser)
# -----------------------------------------------------------------
    # get kooora_check_tittle function from CheckTittle page
    checkTittle = CheckTittle(browser)
# -----------------------------------------------------------------
    # get kooora_scroll_down function from ScrollDown page
    scroll_down = ScrollDown(browser)
# -----------------------------------------------------------------
    # get kooora_scroll_down function from ScrollDown page
    scroll_up = ScrollUp(browser)
# -----------------------------------------------------------------
    # get kooora_using_policy function from UsingPolicy page
    usingPolicy = UsingPolicy(browser)
# -----------------------------------------------------------------
    # get go_to_The_page function from page GO_TO_THE_PAGE page
    go_to_page = GO_TO_THE_PAGE(browser)
# -----------------------------------------------------------------
    # get kooora_games_get_information function from GetInfo page
    get_info = GetInfo(browser)
# -----------------------------------------------------------------

    # load the page
    load_Website.load()

    # scroll down
    scroll_down.kooora_scroll_down(browser)

    # scroll up
    scroll_up.kooora_scroll_up(browser)

    # scroll down
    scroll_down.kooora_scroll_down(browser)

    # using policy
    usingPolicy.kooora_using_policy()

    # check if we are in using policy page
    checkTittle.kooora_check_tittle("شروط الاستخدام")

    # load the page
    load_Website.load()

    # load the games page
    go_to_page.go_to_The_page("مباريات")

    # load the game of today
    go_to_page.go_to_The_page("مباريات اليوم")

    # check if we are in using today games page
    checkTittle.kooora_check_tittle("مباريات اليوم")

    # load the games of English_Premier_League
    go_to_page.go_to_The_page("الدوري الإيطالي الدرجة A")

    # load the name of the first best player
    get_info.kooora_games_get_information()

    # load the page
    load_Website.load()

