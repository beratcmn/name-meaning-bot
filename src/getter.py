import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time
import re

site_url = "https://budizzz.com/pages/isimler-ve-anlamlari"

current_path = os.path.dirname(__file__)

webdriver_path = current_path + "/chromedriver.exe"

driver = webdriver.Chrome(executable_path=webdriver_path)
# driver.minimize_window()
driver.get(site_url)

time.sleep(3)

page_content = driver.find_element(By.XPATH, '//*[@id="nt_content"]/div[2]/div/div[2]')

raw_name_data = page_content.text

driver.quit()

# time.sleep(1)

file = open("./assets/names.txt", "w", encoding="utf-8")

pattern = r'. (ile başlayan isimler)'
raw_name_data = re.sub(pattern, '', raw_name_data)
raw_name_data = raw_name_data.replace("--> Detaylı Bilgi...", "")
raw_name_data = raw_name_data.strip()

lines = raw_name_data.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]

final_data = ""
for line in non_empty_lines:
    final_data += line + "\n"

file.write(final_data)
file.close()
