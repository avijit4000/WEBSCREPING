import pandas as pd
import numpy as np

df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[2,7,3,23],[3,6,8,23],[23,23,63,12]],columns=['A1','B1','C1','D1'])
print(df)
df.to_csv('export.csv')