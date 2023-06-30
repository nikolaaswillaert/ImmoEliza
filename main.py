import utils.get_dataset as getdata
import utils.clean_dataset as cleandata
import pandas as pd

# Get the raw data
dataset = getdata.create_dataframe()

# Clean up the dataset
df = pd.read_csv(r".\data_output\dataframe.csv")
cleaned_csv = cleandata.clean_dataset(df)
cleaned_csv.to_csv(r'.\data_output\cleaned.csv', index = True)
print(cleaned_csv)
