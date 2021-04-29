import time
import os
import json
import sys
import random


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#bekleme sürelerimiz
discord_input_write_sleep = 0.8
discord_input_wait = 2.5
discord_click_wait = 0.5

# sitenin url adresi
discord_login = 'https://discord.com/login'


# Xpathlerimiz

discord_user_epost_input = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input'
discord_user_passw_input = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input'
discord_login_btn = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]'
discord_logout_btn = '//*[@id="app-mount"]/div[3]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[32]'

discord_user_setting_btn = '//*[@id="app-mount"]/div[3]/div/div[2]/div/div/div/div/div[1]/section/div[3]/div[3]/button[3]'
discord_gift_env_btn = '//*[@id="app-mount"]/div[3]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[10]'

discord_gift_code_entry = '//*[@id="app-mount"]/div[3]/div/div[2]/div[2]/div/div[2]/div/div/main/div[1]/div/form/div/div/input'
discord_take_gift_btn = '//*[@id="app-mount"]/div[3]/div/div[2]/div[2]/div/div[2]/div/div/main/div[1]/div/form/div/button'


# karakterlerimiz
chars = 'QWERTYUIOPİLKJHGFDSAZXCVBNMqwertyuıopilkjhgfdsazxcvbnnm123456789'

# kodu kullanıp kullanmadığımızı anlamak için listeye kayıt edelim
used_gift_code = []

# boolean ve integer ve string değişkenlerimiz
start_stop = True
log_counter = 30
gift_code_str = ''



# driverla bağlantısını kurmasını sağlıyoruz
driver = webdriver.Chrome()
#bağlanacağımız url
driver.get(discord_login)

wait = WebDriverWait(driver, timeout=6000)

# Hesabımızla oturum açtıralım
input('karekodu okutunca enter a basın')

# Ayarlara Giriş yapalım
user_stng = driver.find_element_by_xpath(discord_user_setting_btn)
user_stng.click()
time.sleep(discord_click_wait)

# her 30 da bir durdurulsun mu diye sorsun
while start_stop == True:
    if log_counter == 30:
        ask_for_stopping = str(input('işlem durdurulsun mu Y/N'))
        if ask_for_stopping != ('Y' or 'N'):
            print('işlem devam ettiriliyor')
        else:
            with open('used_gift_code.txt','w',encoding='utf-8') as ugc:
                for i in used_gift_code:
                    ugc.write(i+' |\n')
                ugc.close()
            print('Kayıt Tamamlandı..')
            input("çıkış için enter'layın")
            start_stop = False
    else:
        None
