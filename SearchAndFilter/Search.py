import pandas as pd
import numpy as np

excel_files = ['Store1.xlsx', 'Store2.xlsx']

merge = pd.DataFrame()

for file in excel_files:
  df = pd.read_excel(file)
  #Get total where name = popcorn
  popcorn = df['Total'].where(df['Name'] == 'Popcorn').dropna()
  print(file)
  print(popcorn)