from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import ElementClickInterceptedException

INSTA_LOGIN = ""
INSTA_PASSWORD=""
SIMILAR_ACCOUNT=""

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")  

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Разрешить все cookie')]"))).click()
        input_login = self.driver.find_element(by=By.NAME, value="username")
        input_password = self.driver.find_element(by=By.NAME, value="password")
        input_login.send_keys(INSTA_LOGIN)  
        input_password.send_keys(INSTA_PASSWORD)
        time.sleep(5)
        input_password.send_keys(Keys.ENTER)
        time.sleep(5)
#new_driver.find_element(By.XPATH, "//button[contains(., 'Сохранить данные')]").click() #optional

#new_driver.find_element(By.XPATH, "//button[contains(., 'Не сейчас')]").click()    #optional


    def find_followers(self):
       self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")  
       time.sleep(10)
       self.driver.find_element(By.XPATH, "//a[contains(@href, 'followers')]").click()
       time.sleep(5)
   


#Follow all followers
    def follow(self):   
        #in progress
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()


    


