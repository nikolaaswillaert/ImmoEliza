import utils.get_dataset as getdata
import utils.clean_dataset as cleandata
import pandas as pd
from pathlib import Path

# Build path to file
# Selects current working directory
cwd = Path.cwd()
csv_path = 'data_output/dataframe.csv'
csv_cleaned_path = 'data_output/dataframe_cleaned.csv'
src_path = (cwd / csv_path).resolve()
out_path = (cwd / csv_cleaned_path).resolve()

# Get the raw data
dataset = getdata.create_dataframe()

# Clean up the dataset
df = pd.read_csv(src_path)
cleaned_csv = cleandata.clean_dataset(df)
cleaned_csv.to_csv(out_path)
print(cleaned_csv)
