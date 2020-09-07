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
print("First 5 rows: ", f500.head(5))


# We can use the DataFrame.dtypes attribute to return information about the type of each column.
print(f500.dtypes)

# DataFrame.info() method shows an overview of all the dtypes and used in DataFrame, along with its shape and other information

print('')
print("Below is the information of the DataFrame")
print(f500.info())
data_info = f500.info()

# We can select data using DataFrame.loc[]
# dtypes returns information about the type of each column.
# type() function assign the type of objects.
# So, if I would like to know the type of object such as Series, I can use the type() function.

# Select by label
# single column df.loc[:,"col1"]
# List of columns df.loc[:.["col1","col7"]]
# Slice of columns df.loc[:,"col1":"col4"]

countries = f500.loc[:,"country"]
revenues_years = f500.loc[:,["revenues","years_on_global_500_list"]]
ceo_to_sector = f500.loc[:,"ceo":"sector"]

#Choosing single row
single_row = f500.loc["Walmart"]
print(type(single_row))
print(single_row)
# In this case, the dtype of single row is object. It is a series and object.
# It means that the Series not only has numeric values but also string values.

# Series.value_counts() method.
# This method displays each unique non-null value in a column and their counts in order.

sectors = f500.loc[:,"sector"]
sectors_value_counts = sectors.value_counts()
print(sectors_value_counts)

sectors_industries = f500.loc[:,["sector","industry"]]
print(type(sectors_industries))

countries = f500.loc[:,"country"]
country_counts = countries.value_counts()

countries = f500['country']
countries_counts = countries.value_counts()

india = countries_counts.loc["India"]
north_america = countries_counts.loc[["USA","Canada","Mexico"]]

print(north_america)

# I need to check below two lines
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"], ["rank","previous_rank"]]
bottom_companies = f500.loc["National Grid":"AutoNation",["rank","sector","country"]]
