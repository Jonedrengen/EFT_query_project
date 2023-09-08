import pandas as pd


# creating a dataframe from a csv file
df = pd.read_csv('ammo_stats.csv')

# view the first 5 rows of the dataframe
print(df.head(100))


