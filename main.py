import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime

cat = pd.read_csv('./stock_list.csv')
cat = cat.set_index('Ticker')
driver = webdriver.Chrome()
#get current year
now_year = datetime.datetime.now().year
eps_dict = {}
eps_dict['ticker'] = ""
for i in range(1,8):
        eps_dict[now_year-i] = ""

roe_dict = eps_dict

print(eps_dict)

def find_stock_cat(ticker):
        return cat.at[ticker,'Industry']

def find_same_cat(industry):
        return (cat.loc[cat['Industry']== industry]).index

def scrap_all_data(ticker):
        stock_list = find_same_cat(find_stock_cat(ticker)).tolist()
        df = pd.DataFrame()
        print(stock_list)
        for ticker in stock_list:
                print(ticker)
                print(cat.at[ticker,'Exchange'])
                url = "https://www.tradingview.com/symbols/"+cat.at[ticker,'Exchange']+"-"+ticker+"/financials-income-statement/earnings-per-share-diluted/"
                driver.get(url)
                eps_dict['ticker'] = ticker
                for i in range(1,8):
                        eps = driver.find_element_by_xpath('//*[@id="js-category-content"]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div['+str(i+2)+']/div[4]')
                        eps_dict[now_year-i] = eps.text
                print(eps_dict)
                time.sleep(0.3)

        



scrap_all_data('JPM')






