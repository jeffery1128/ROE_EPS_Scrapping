import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


cat = pd.read_csv('./stock_sector.csv')
cat = cat.set_index('Ticker')
driver = webdriver.Chrome()

def find_stock_cat(ticker):
        return cat.at[ticker,'Industry']

def find_same_cat(industry):
        return (cat.loc[cat['Industry']== industry]).index

def scrap_all_data(ticker):
        stock_list = find_same_cat(find_stock_cat(ticker)).tolist()
        print((stock_list))
        



scrap_all_data('TSLA')






