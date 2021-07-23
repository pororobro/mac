from selenium import webdriver
from time import sleep
from creditentials import username, password
from webdriver_manager.chrome import ChromeDriverManager


class InstaUnfollowers:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")
        sleep(2)
        # instagram login
        username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_type.send_keys(password)
        # ad = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        # ad.click()
        log_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        log_in.click()
        sleep(3)
        # next_step = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        # next_step.click()
        # sleep(3)

    

    # def get_people(self,k):
    #     sleep(2)
    #     scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div["+k+"]")
    #     prev_height, height = 0, 1
    #     while prev_height != height:
    #         prev_height = height
    #         sleep(3)
    #         height = self.driver.execute_script("""
    #             arguments[0].scrollTo(0, arguments[0].scrollHeight); 
    #             return arguments[0].scrollHeight;
    #             """, scroll_box)
    #     links = scroll_box.find_elements_by_tag_name('a')
    #     names = [name.text for name in links if name.text != '']
    #     close = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
    #     close.click()
    #     return names

    def send_message(self):
        # change to your username
        self.driver.get("https://www.instagram.com/codingstagram_")
        sleep(2)
        Following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        your_name = self.driver.find_elements_by_xpath("/html/body/div[5]/div/div/div[3]")
        your_name.click()
        # hello = your_name.find_elements_by_tag_name('a')
        # names = [name.text for name in hello]
        # print(names)

        # following = self.get_people(k="3")
        # print(following)
        # Followers = self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
        # Followers.click()
        # followers = self.get_people(k="2")
        # not_following_back = [user for user in following if user not in followers]
        # print(not_following_back)


my_bot = InstaUnfollowers(username, password)
my_bot.send_message()
my_bot.driver.close()

print('owari')