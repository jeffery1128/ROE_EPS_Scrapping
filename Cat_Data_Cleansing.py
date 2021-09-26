import pandas as pd

df = pd.read_csv('./Cat.csv')
df = df.drop_duplicates()
df.columns = df.iloc[0]
df = df[['No.','Ticker','Company', 'Sector','Industry','Country','Market Cap','P/E','Price','Change','Volume']]
df = df.set_index('No.')
df = df.iloc[1:]
#print(df)
df.to_csv('./Cat.csv')