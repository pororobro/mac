from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Soundcloud:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://soundcloud.app.goo.gl/ndZz8")
        sleep(5)
        entering = self.driver.find_element_by_css_selector("#onetrust-accept-btn-handler")
        entering.click()
        sleep(5)
        play_song = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]')
        play_song.click()
        sleep(30)
        self.driver.quit()

my_bot = Soundcloud()