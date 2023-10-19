import pandas as pd 

data = pd.read_csv('csv_data.csv')

data1 = data['Dato_2']


print(f'datos 2 = \n{data1}')
