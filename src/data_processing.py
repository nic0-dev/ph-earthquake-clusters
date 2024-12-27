# Data Cleaning Script
import pandas as pd
import numpy as np

def load_data(file_path):
  # Load earthquake CSV to DataFrame
  df = pd.read_csv(file_path)
  return df

def clean_data(df):
  # Convert data string to datetime
  df["Date_Time"] = pd.to_datetime(df["Date_Time_PH"], errors='coerce')

  # Dropping/Imputing missing values
  df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

  return df

if __name__=="__main__":
  data = load_data("../data/phivolcs_earthquake_data.csv")
  data = clean_data(data)
  print(data)
  