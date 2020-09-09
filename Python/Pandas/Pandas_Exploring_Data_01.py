import pandas as pd

f500 = pd.read_csv('C:/Users/Jay/Documents/GitHub/DataQuest/Python/Pandas/DB/f500.csv', index_col=0)

#choose first 10 rows
f500_head = f500.head(10)

#Display the information of DataFrame
f500.info()

#Using the vectorization, we can calculate fast using Pandas
rank_change = f500["previous_rank"]-f500["rank"]

#using some methods, we can find the values
rank_change =  f500["previous_rank"] - f500["rank"]

rank_change_max = rank_change.max()
print("Biggest increase in rank : ", rank_change_max)
rank_change_min = rank_change.min()
print("Biggest decrease in rank : ", rank_change_min)

#Using the describe method, we can check the details of series.
assets = f500["assets"]
print(assets.describe())

country = f500["country"]
print(country.describe())

rank = f500["rank"]
rank_desc = rank.describe()

prev_rank = f500['previous_rank']
print(prev_rank.describe())
prev_rank_desc=prev_rank.describe()