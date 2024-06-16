import time
import json
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# 設定ファイルの読み込み
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

chrome_debugger_address = config['chrome_debugger_address']
chrome_driver_path = config['chrome_driver_path']
url = config['url']
date_value = config['date_value']
time_value = config['time_value']
specified_time_jst_str = config['specified_time_jst']
webdriver_wait_time = config['webdriver_wait_time']

# 日本時間で指定時刻を設定
jst = timezone(timedelta(hours=+9), "JST")
specified_time_jst = datetime.fromisoformat(specified_time_jst_str).replace(tzinfo=jst)

# Chromeオプションを設定
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", chrome_debugger_address)

# Chromeドライバーを作成
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options)

# 指定時刻まで待機
while datetime.now(jst) < specified_time_jst:
    time.sleep(1)

# 指定のURLにアクセス
driver.get(url)

# Select要素を取得1
select_element = WebDriverWait(driver, webdriver_wait_time).until(EC.presence_of_element_located((By.ID, "play_date")))
actions = ActionChains(driver)
actions.move_to_element(select_element).perform()

# 特定の値を選択する1
select_option = WebDriverWait(driver, webdriver_wait_time).until(EC.presence_of_element_located((By.XPATH, f"//select[@id='play_date']/option[@value='{date_value}']")))
select_option.click()

# Select要素を取得2
select_element2 = WebDriverWait(driver, webdriver_wait_time).until(EC.presence_of_element_located((By.ID, "play_time")))
select_element2.click()

# 特定の値を選択する2
select_option2 = WebDriverWait(driver, webdriver_wait_time).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{time_value}']")))
select_option2.click()

# 指定のclass要素の<div>に含まれ、onclickが定義された<img>をクリック
div_element = WebDriverWait(driver, webdriver_wait_time).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_Booking")))
img_element = div_element.find_element(By.TAG_NAME, "img")
driver.execute_script("arguments[0].click();", img_element)