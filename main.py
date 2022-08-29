import pandas as pd
a=(input('введите город'))
df = pd.read_excel('1.xlsx')
#print(df['город'])
print(df[df['город']== a ])

#print(data[data=='1'])
#print(data.loc[data['город']=='1'])
# Print the content
#print("The content of the file is:\n", data)
#print(data.loc)
#data[(['Город'] == 'Пермь')]