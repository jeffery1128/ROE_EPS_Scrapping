from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
driver.get('https://finviz.com/screener.ashx?v=111')
total = (driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[3]/td/table/tbody/tr/td[1]')).text
press_time = int(total[7:11])/20
print(press_time)
Cat = pd.DataFrame()
#soup=BeautifulSoup(html,'html.parser')
#tb = soup.find_all('table')
#target = tb[16]
#print(target)
tb = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table')
html_tb = tb.get_attribute('innerHTML')
html_tb = '<table>' + html_tb + '</table>'
df = pd.read_html(html_tb)
pd.concat([Cat,df])
#print(df)
next_button = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[3]/td/table/tbody/tr/td[5]/a')
next_button.click()

#tb = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table')
#html_tb = tb.get_attribute('innerHTML')
#html_tb = '<table>' + html_tb + '</table>'
#df = pd.read_html(html_tb)
#tb = soup.find_all('tbody')
#screener-content > table > tbody > tr:nth-child(4) > td > table

#table = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table')
#print(table.text)