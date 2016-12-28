#from urllib.request import urlopen
#from bs4 import BeautifulSoup
import pandas as pd
#import html5lib

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
url = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015'
df = pd.read_html(url)[0]
#print(df)
#print(type(df))

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
"""df.columns = ['Rank', 'Player', 'Team', 'Games_Played', 'Goals', 'Assists', 'Points', 
'Plus_Minus_Rating', 'Penaly_Minutes', 'Points_per_Game', 'Shots_on_Goal', 
'Shooting_Percentage', 'Game-Winnig_Goals', 'Power-Playing_Goals', 
'Power-Playing_Assists', 'Short-Handed_Goals', 'Short-Handed_Assists']"""
df.columns = (['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 
'SOG', 'PCT', 'GWG', 'G', 'A', 'G', 'A'])
#print(df)

# TODO: Get rid of any row that has at least 4 NANs in it
#
df = df.dropna(axis=0, thresh=4)
#print(df)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
df = df.drop_duplicates(subset=['PLAYER', 'TEAM', 'PTS/G'])
df.drop(df.index[0], inplace=True)
#print(df)

# TODO: Get rid of the 'RK' column
#
#df = df.fillna(method='ffill')
df = df.drop(labels=['RK'], axis=1)
#print(df)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop=True)
#print(df)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df = df.convert_objects(convert_numeric=True)
#print(df.dtypes)


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print(len(df))
#print(df.index)
#print(df.PCT.unique())
#print(len(df.PCT.unique()))
#sag = df.loc[15, ['GP']] + df.loc[16, ['GP']]
#sag = df.loc[15:16, ['GP']]
sag = int(df.loc[15, ['GP']]) + int(df.loc[16, ['GP']])
print(sag)

