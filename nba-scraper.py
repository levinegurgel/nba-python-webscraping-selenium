import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
import json

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

#option = Options()
#option.headless = True

PATH = "/opt/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get(url)


time.sleep(10)

driver.find_element_by_xpath("div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

driver.quit()


