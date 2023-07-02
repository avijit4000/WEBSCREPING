from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd

website='https://www.google.com/finance/markets/most-active?authuser=0'
result=re.get(website)
console=result.text
soup=bs(console,'lxml')

box=soup.find('ul', class_='sbnBtf')

box_2=box.find_all('li')
# print(box_2)
df=[]
for i in box_2:
    a=[[i.find('div',class_="ZvmM7").text], [i.find('div',class_="YMlKec").text]]
    df.append(a)
data=pd.DataFrame(df)
data.to_csv('data.csv')