# 구글 트렌드 인기 검색어 가져오기

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome('../chromedriver')

url = 'https://trends.google.com/trends/yis/2020/KR/'
driver.get(url)

## 종합 더보기 버튼 : //*[@id="anchorName"]/div/div/div[2]/div[1]
## 게임 더보기 버튼 : //*[@id="anchorName"]/div/div/div[2]/div[1]

xpath = '//*[@id="anchorName"]/div/div/div[2]/div[1]'

sel_ele = driver.find_elements_by_xpath(xpath)
len(sel_ele)

time.sleep(3)
sel_ele[0].click()
time.sleep(3)
sel_ele[3].click()

page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title


dat = soup.find_all("div", class_='fe-expandable-item-text')
len(dat)

dat_all = soup.find_all("div", class_="fe-expandable-list-content")
len(dat)


tmp = dat_all[0].find_all("div", class_='fe-expandable-item-text')
all_info = []
for one in tmp:
    # print(one.div.text)
    all_info.append(one.div.text)

all_info

tmp = dat_all[3].find_all("div", class_='fe-expandable-item-text')
all_game = []
for one in tmp:
    # print(one.div.text)
    all_game.append(one.div.text)

all_game

num = list(range(1, 11, 1) )
num
