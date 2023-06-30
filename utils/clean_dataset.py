import pandas as pd
import numpy as np

def clean_dataset(df):
    #REMOVE ALL THE EMPTY LINES
    rows_to_remove = []
    for index, row in df.iterrows():
        if row.isnull().all():
            rows_to_remove.append(index)

    df = df.drop(rows_to_remove)
    
    # Locality
    # !!! CONVERT THE CITIES INTO COORDINATES

    # Type of property (House/apartment)
    
    # Subtype of property (Bungalow, Chalet, Mansion, ...)

    # Price

    # Type of sale (Exclusion of life sales

    # Open fire (Yes/No)

    # Number of rooms

    # Living Area

    # Fully equipped kitchen (Yes/No)

    # Furnished (Yes/No)

    # Terrace (Yes/No)
    # If yes: Area

    # Garden (Yes/No)
    # If yes: Area

    # Surface of the land

    # Surface area of the plot of land

    # Number of facades

    # Swimming pool (Yes/No)

    # State of the building (New, to be renovated, ...)

def analyze_column(df, column_name):
    column = df[column_name]
    num_nan = column.isnull().sum()
    num_unique = column.nunique()
    unique_values = column.unique()
    percentage_nan = (num_nan / len(column)) * 100
    percentage_unique = (num_unique / len(column)) * 100
    print(f"Analysis for column '{column_name}':")
    print(f"Number of NaN values: {num_nan}")
    print(f"Number of unique values: {num_unique}")
    print(f"Percentage of NaN values: {percentage_nan:.2f}%")
    print(f"Percentage of unique values: {percentage_unique:.2f}%")
    print(f"Unique values: {unique_values}")


