import openpyxl

excel_files = ['Store1.xlsx', 'Store2.xlsx']

for file in excel_files:
  wb = openpyxl.load_workbook(file)
  worksheet = wb["MovieStandSales"]
  worksheet['D11'] = '=SUM(D2:D10)'
  wb.save(file)