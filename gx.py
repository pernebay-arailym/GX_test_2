import great_expectations as gx
import pandas as pd

df =pd.read_csv("https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv")

#data context is an entry point to GX functionally
context = gx.get_context()

#connect data and create a Batch 
data_sources = context.data_sources.add_pandas("pandas")
data_assets = data_sources.add_dataframe_asset(name = "pd datafrmae asset")

batch_definition = data_assets.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.add_batch(batch_parametres = {"dataframe": df})