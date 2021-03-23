import openpyxl
#pip3 install openpyxl

excel_files = ['Store1.xlsx','Store2.xlsx']

values = []

for file in excel_files:
  workbook = openpyxl.load_workbook(file)
  worksheet = workbook['MovieStandSales']
  cell_value = worksheet['D2'].value
  values.append(cell_value)

  print(cell_value)