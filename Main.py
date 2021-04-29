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
write_sleep = 0.005

# sitenin url adresi
discord_login = 'https://discord.com/login'


# Xpathlerimiz

discord_user_epost_input = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input'
discord_user_passw_input = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input'
discord_login_btn = '//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]'
discord_logout_btn = '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[28]'

discord_user_setting_btn = '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[3]/button[3]'
discord_gift_env_btn = '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[10]'

discord_gift_code_entry = '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/main/div[1]/div/form/div/div/input'
discord_take_gift_btn = '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/main/div[1]/div/form/div/button'


# karakterlerimiz
chars = 'QWERTYUIOPİLKJHGFDSAZXCVBNMqwertyuıopilkjhgfdsazxcvbnnm123456789'

# kodu kullanıp kullanmadığımızı anlamak için listeye kayıt edelim
used_gift_code = []

# boolean ve integer ve string değişkenlerimiz
start_stop = True
diff_code = True
log_counter = 0
denen = 0
gift_code_str = ''

stop_loop = 2500

# driverla bağlantısını kurmasını sağlıyoruz
driver = webdriver.Chrome()
#bağlanacağımız url
driver.get(discord_login)

wait = WebDriverWait(driver, timeout=6000)

# Hesabımızla oturum açtıralım
input('karekodu okutunca enter a basın')

# Fonksiyonlar
def code_generator():
    gift_code = random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + '-' + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + '-' + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + '-' + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars)
    return  gift_code

# Ayarlara Giriş yapalım
try:
    user_stng = driver.find_element_by_xpath(discord_user_setting_btn)
    user_stng.click()
    time.sleep(discord_click_wait)
    gift_inv = driver.find_element_by_xpath(discord_gift_env_btn)
    gift_inv.click()
    time.sleep(discord_click_wait)
except:
    print('olmadı')
# her 30 da bir durdurulsun mu diye sorsun
while start_stop == True:
    if log_counter == stop_loop:
        ask_for_stopping = str(input('işlem durdurulsun mu Y/N'))

        if ask_for_stopping == 'Y':
            with open('used_gift_code.txt', 'w', encoding='utf-8') as ugc:
                for i in used_gift_code:
                    ugc.write(i + ' |\n')
                ugc.close()
            print('Kayıt Tamamlandı..')
            logg_out = driver.find_element_by_xpath(discord_logout_btn)
            logg_out.click()
            time.sleep(discord_click_wait)
            input("çıkış için enter'layın")
            start_stop = False
            os.system("taskkill /F /im chromedriver.exe")
        elif ask_for_stopping == 'N':
            print('işlem devam ediyor')
            log_counter = 0
    else:
        code_gift = random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + '-' + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + '-' + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + '-' + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars)
        if code_gift in used_gift_code:
            pass
        else:
            used_gift_code.append(code_gift)

            code_write = driver.find_element_by_xpath(discord_gift_code_entry)
            code_write.send_keys(code_gift+Keys.ENTER)
            time.sleep(write_sleep)

            code_ok = driver.find_element_by_xpath(discord_take_gift_btn)
            code_ok.click()
            time.sleep(write_sleep)

            denen+=1
            print(str(denen)+' | '+code_gift)
            log_counter += 1
            code_gift = ''
            code_write.clear()
