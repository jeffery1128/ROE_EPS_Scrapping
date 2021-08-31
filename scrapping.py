from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
driver.get('https://finviz.com/screener.ashx?v=111')
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
tb = soup.find_all('table')
soup=BeautifulSoup(tb[17].text,'html.parser')
print(type(tb[17]))
#tb = soup.find_all('tbody')


#table = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table')
#print(table.text)