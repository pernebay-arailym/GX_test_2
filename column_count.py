import pandas as pd

#load the csv file
url="https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
df = pd.read_csv(url)

list = df.columns.tolist()
print("Column names in the dataframe:", list)
#count how many times the value 1 appears in the 'passanger_count' column
count = (df['passenger_count']==1).sum()
print("Number of occurances of '1' in 'passenger column':", count)