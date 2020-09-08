import pandas as pd

f500 = pd.read_csv('C:/Users/Jay/Documents/GitHub/DataQuest/Python/Pandas/DB/f500.csv', index_col=0)

#choose first 10 rows
f500_head = f500.head(10)

#Display the information of DataFrame
f500.info()
