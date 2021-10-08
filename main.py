import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

cat = pd.read_csv('./stock_list.csv')
cat = cat.set_index('Ticker')
driver = webdriver.Chrome()
#get current year
now_year = datetime.datetime.now().year

def find_stock_cat(ticker):
        return cat.at[ticker,'Industry']

def find_same_cat(industry):
        return (cat.loc[cat['Industry']== industry]).index

def scrap_all_data(ticker):
        stock_list = find_same_cat(find_stock_cat(ticker)).tolist()
        result = {}
        eps_dict = {}
        for i in range(1,8):
                eps_dict[now_year-i] = ""
        print(stock_list)
        for ticker in stock_list:
                print(ticker)
                print(cat.at[ticker,'Exchange'])
                print(str(stock_list.index(ticker)+1),'/',len(stock_list))
                url = "https://www.tradingview.com/symbols/"+cat.at[ticker,'Exchange']+"-"+ticker+"/financials-income-statement/earnings-per-share-diluted/"
                driver.get(url)
                time.sleep(0.8)
                #eps_dict['ticker'] = ticker
                for i in range(1,8):
                        try:
                                eps = driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div['+str(i+2)+']/div[4]')
                                eps_dict[now_year-i] = (eps.text).replace('\u202a','').replace('\u202c','')
                        except:
                                print('Page not found')
                print(eps_dict)
                result[ticker] = eps_dict
                eps_dict={}
                time.sleep(0.1)
        return result

        
result = scrap_all_data('AAL')

df= pd.DataFrame.from_dict(result)
df = df.T
print(df)
sns.barplot(data = df , x=[2020,2019,2018,2017,2016,2015,2014],y="Ticker" , hue = "ticker")
plt.show()






