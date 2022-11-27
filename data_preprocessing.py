# %%
import numpy as np
import pandas as pd


data = pd.read_csv("STAT3613+Group+Project.csv")
data = data.drop(data[data['Finished'] == '0'].index)
data_col_name = ['Gender',	'Year of Study',	'Monthly Expense',	'Living District',	'Transportation',	'Num_transfer',	'Time',	'Comfortability',	'Price',	'Walking Distance',	'Acceptable price',	'MTR',	'Bus',	'Shuttle Bus',	'Taxi',	'Tram']
data = data.drop([0, 1], axis = 0)
data = data.iloc[:,18:]
data = data.drop(['Q7_5_TEXT', 'Q7_5','Q5_6_TEXT'], axis= 1)
CA_raw = data.loc[:, 'Q8_1_1': 'Q8_5_6']
data = data.drop(data.loc[:, 'Q8_1_1': 'Q8_5_6'], axis = 1)
data.columns= data_col_name
CA_raw = CA_raw.fillna(0)
CA_raw = CA_raw.astype(int)
count = CA_raw.sum()
CA = np.zeros((5, 6))

for i, val  in enumerate(count):
    CA[i//6, i%6] = int(val)
CA = pd.DataFrame(CA)
CA.columns = ['Fast', 'Con', 'Seat', 'Transfer', 'Price', 'Walk']
CA.index = ['MTR', 'Bus', 'Shttle', 'Taxi', 'Tram']


# %%
data.to_csv('data.csv')
CA.to_csv('CA.csv')
# %%
