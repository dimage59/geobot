import openpyxl
a=("П")
wookbook = openpyxl.load_workbook("1.xlsx")
worksheet = wookbook.active
#print(worksheet[1][0].value)
for row in range(1,worksheet.max_row+1):
    city = worksheet[row][0].value
    number = worksheet[row][1].value
    index=city.find(a)
    print(index)
    print(city)
