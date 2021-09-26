from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup
import time
#chop = webdriver.ChromeOptions()
#chop.add_extension('./adblock.crx')
#time.sleep(20)
driver = webdriver.Chrome()
driver.get('https://finviz.com/screener.ashx?v=111')
total = (driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[3]/td/table/tbody/tr/td[1]')).text
press_time = int(total[7:11])
press_time = round(press_time/20) + (press_time%20 > 0)
print(press_time)
Cat = pd.DataFrame()

for i in range(press_time+1):
        print(i)
        try:
                tb = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table')
                html_tb = tb.get_attribute('innerHTML')
                html_tb = '<table>' + html_tb + '</table>'
                df = pd.read_html(html_tb)
                Cat = Cat.append(df)
                next_button = driver.find_element_by_xpath('//*[@id="screener-content"]/table/tbody/tr[3]/td/table/tbody/tr/td[5]/a')
                next_button.click()
        except:
                print(Cat)
                cross = driver.find_element_by_xpath('//*[@id="modal-elite-ad-close"]')
                cross.click()
        time.sleep(0.5)

print(Cat)
Cat.to_csv('./Cat.csv')