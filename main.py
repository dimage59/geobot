import openpyxl
wookbook = openpyxl.load_workbook("1.xlsx")
worksheet = wookbook.active
for i in range(0, worksheet.max_row):
    for col in worksheet.iter_cols(1, worksheet.max_column):
        print(col[i].value, end="\t\t")
    print('')