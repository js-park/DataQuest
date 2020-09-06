# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:52:34 2020

@author: Jay
"""

import pandas as pd

f500 = pd.read_csv('C:/Users/Jay/Documents/GitHub/DataQuest/Python/Pandas/DB/f500.csv', index_col=0)

# We can use type function to know the data type
# We can use .shape attribute to check the shape of data
print(f500.shape)

# DataFrame can contain columns with multiple data type: numeric, string, boolean.

# We can check the data using head() method and tail() method
# Check first 5 rows.
print('First 5 rows: ', f500.head(5))


# We can use the DataFrame.dtypes attribute to return information about the type of each column.
print(f500.dtypes)

# DataFrame.info() method shows an overview of all the dtypes and used in DataFrame, along with its shape and other information

print('')
print('Below is the information of the DataFrame')
print(f500.info())
