import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


class scrapper:

        def __init__(self):
                cat = pd.read_csv('./stock_list.csv')
                cat = cat.set_index('Ticker')
                self.stock_cat_df = cat
                self.driver = webdriver.Chrome()


        def find_stock_cat(self,ticker):
                return self.stock_cat_df.at[ticker,'Industry']

        def find_same_cat(self,industry):
                return (self.stock_cat_df.loc[self.stock_cat_df['Industry']== industry]).index

        def scrap_all_eps(self,ticker):
                stock_list = self.find_same_cat(self.find_stock_cat(ticker)).tolist()
                result = {}
                eps_dict = {}
                #get current year
                now_year = datetime.datetime.now().year
                for i in range(1,8):
                        eps_dict[now_year-i] = ""
                print(stock_list)
                for ticker in stock_list:
                        print(ticker)
                        print(self.stock_cat_df.at[ticker,'Exchange'])
                        print(str(stock_list.index(ticker)+1),'/',len(stock_list))
                        url = "https://www.tradingview.com/symbols/"+self.stock_cat_df.at[ticker,'Exchange']+"-"+ticker+"/financials-income-statement/earnings-per-share-diluted/"
                        self.driver.get(url)
                        time.sleep(0.8)
                        #eps_dict['ticker'] = ticker
                        for i in range(1,8):
                                try:
                                        eps = self.driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div['+str(i+2)+']/div[4]')
                                        eps_dict[now_year-i] = (eps.text).replace('\u202a','').replace('\u202c','')
                                except:
                                        print('Page not found')
                        print(eps_dict)
                        result[ticker] = eps_dict
                        eps_dict={}
                        time.sleep(0.1)
                return result

        
#result = scrap_all_eps('AAL')

#df= pd.DataFrame.from_dict(result)
#df = df.T
#print(df)
scrapper = scrapper()

result = scrapper.scrap_all_eps("AAL")
df= pd.DataFrame.from_dict(result)
df = df.T
print(df)







