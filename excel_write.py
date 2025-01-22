from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet.title = "Sample Excel Sheet"

sheet["A1"] = "Kalai"
sheet["B1"] = 43
sheet["C1"] = 'TX'

wb.save("D:/Excel/writeme.xlsx")
