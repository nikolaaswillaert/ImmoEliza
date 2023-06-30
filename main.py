import utils.get_dataset as getdata
import utils.clean_dataset as cleandata
import pandas as pd

#dataset = getdata.create_dataframe()
#cleandata.clean_dataset(dataset)
df = pd.read_csv("/home/niko/Desktop/GitHub Projects/ImmoEliza/data_output/dataframe_20k_280623.csv")
a = cleandata.clean_dataset(df)
print(a)
