# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv(r'direct_marketing.csv', sep = ',')

#print (df)
#print (df.recency)
#print (df['recency'])
#print (df[['recency']])
#print (df.loc[:, 'recency'])
#print (df.loc[:, ['recency']])
#print (df.iloc[:, 0])
#print (df.iloc[:, [0]])
#print (df.ix[:, 0])
#print (df[0:2])
#print (df.iloc[0:2, :])
#print(df.loc[0:4, ['recency', 'history', 'mens', 'womens']])
#print(df[df.recency < 7])
#use | instead of 'or'
print(df[(df.recency < 7) | (df.zip_code == 'Surburban')])
#use & instead of 'and'
print(df[(df.recency < 7) & (df.zip_code == 'Surburban')])
