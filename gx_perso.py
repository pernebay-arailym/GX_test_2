import great_expectations as ge
import pandas as pd 
from pathlib import Path

df =pd.read_csv("https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv")

#create GX DataFrame from Pandas DataFrame
gx_test = ge.from_pandas(df)

#define expectations on GX DataFrame
gx_test.expect_column_values_to_be_between(column = "passenger_count", min_value =2, max_value=6)
gx_test.expect_column_values_to_not_be_null(column = "vendor_id")
gx_test.expect_column_values_to_be_unique(column= "vendor_id")
gx_test.expect_column_values_to_be_in_set(column = "payment_type", value_set =[1,2,3,4,5])
gx_test.expect_column_values_to_be_in_set(column= "pickup_location_id", value_set =[13] )

#view results
results = gx_test.validate()

#save results in the folder
Path("results").mkdir(exist_ok=True)

with open("results/validation_results.txt", "w") as f:
    f.write(str(results))