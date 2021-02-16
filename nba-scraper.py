import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

PATH = "/opt/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get(url)

#time.sleep(10)
#driver.find_element_by_xpath("div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

time.sleep(10)

driver.find_element_by_id("onetrust-accept-btn-handler").click()

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)

driver.quit()


