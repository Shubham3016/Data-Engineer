# import pandas as pd
# import os

# # Get the file path
# file_path = r'C:\PYTHON_LEARNING\.venv\BlinkIT Grocery Data.xlsx'

# # Check if file exists
# if os.path.exists(file_path):
#     # Read the Excel file
#     df = pd.read_excel(file_path)
    
#     # Display basic information
#     print("Dataset Shape:", df.shape)
#     print("\nFirst few rows:")
#     print(df.head())
    
#     print("\nDataset Info:")
#     print(df.info())
    
#     print("\nBasic Statistics:")
#     print(df.describe())
# else:
#     print(f"File not found: {file_path}") 



import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


print(pandas.__version__)


import pandas as pd
a=[1,2,3,4,5,6]


mds=pd.Series(a)
print(mds)



import pandas as pd

a=[1,2,3,4,5,6]

md=pd.Series(a,index=["a","b","c","d","e","f"])

print(md)


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
