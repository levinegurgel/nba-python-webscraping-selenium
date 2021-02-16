import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json


url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

top10ranking = {}

rankings = {
        '3points': {'field':'FG3M','label':'3PM'},
        'points':{'field': 'PTS','label': 'PTS',},
        'assistants':{'field': 'AST','label':'AST',},
        'rebounds':{'field':'REB','label':'REB',},
        'steals':{'field': 'STL','label': 'STL',},
        'blocks':{'field': 'BLK','label': 'BLK',},
}

def buildrank(type):

        field = rankings[type]['field']
        label = rankings[type]['label']

        driver.find_element_by_xpath(
                f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()

        element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
        html_content = element.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        df_full = pd.read_html(str(table))[0].head(10)
        df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
        df.columns = ['pos', 'player', 'team', 'total']

        #print(top10ranking)        

        return df.to_dict('records')

PATH = "/opt/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get(url)

time.sleep(10)
driver.find_element_by_id("onetrust-accept-btn-handler").click()

for k in rankings:
                top10ranking[k] = buildrank(k)

driver.quit()

js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()