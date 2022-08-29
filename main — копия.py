import openpyxl
a=("П")
wookbook = openpyxl.load_workbook("1.xlsx")
worksheet = wookbook.active
#print(worksheet[1][0].value)
for row in range(1,worksheet.max_row+1):
    city = worksheet[row][0].value
    number = worksheet[row][1].value
#    index=city.find(a)
    print(index)
    print(city)



import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel('1.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['город', 'Телефон'])
print(data[data=='1'])
#print(data.loc[data['город']=='1'])
# Print the content
#print("The content of the file is:\n", data)
#print(data.loc)
#data[(['Город'] == 'Пермь')]