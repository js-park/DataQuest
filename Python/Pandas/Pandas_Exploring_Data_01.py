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

# The method chaining skill
countries_counts = f500["country"].value_counts()

#More specifically
print('The number of firms from China: ', f500["country"].value_counts().loc["China"])

#Finding the number of values that have 0 in previous year
zero_previous_rank = f500["previous_rank"].value_counts().loc[0]
print("Zero Previous Year: ", f500["previous_rank"].value_counts().loc[0])

#Finding max values from numeric value columns
max_f500 = f500.max(numeric_only=True)

# The describe method is only for numeric columns
# In order to use the describe for non numeric, we need to put (include=['O'])

# Assignment
top5_rank_revenue=f500.loc[:,["rank","revenues"]].head(5)
print(top5_rank_revenue)

top5_rank_revenue.loc["State Grid","revenues"]=999
print(top5_rank_revenue)

# Assigning new values in cell
f500.loc["Dow Chemical","ceo"]="Jim Fitterling"

# Use boolean indexing to change all rows that meet the same criteria.
#Making boolean Series first, and apply it on loc.

motor_bool = f500["industry"] == "Motor Vehicles and Parts"

motor_countries = f500.loc[motor_bool, "country"]