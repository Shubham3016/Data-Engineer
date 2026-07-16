import pandas as pd
import os

# Get the file path
file_path = r'C:\PYTHON_LEARNING\.venv\BlinkIT Grocery Data.xlsx'

# Check if file exists
if os.path.exists(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Display basic information
    print("Dataset Shape:", df.shape)
    print("\nFirst few rows:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nBasic Statistics:")
    print(df.describe())
else:
    print(f"File not found: {file_path}") 