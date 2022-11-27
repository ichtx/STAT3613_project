# %%
import numpy as np
import pandas as pd


data = pd.read_csv("raw.csv")
data = data.drop(data[data['Finished'] == '0'].index)
data_col_name = ['Gender',	'Year of Study',	'Monthly Expense',	'Living District',	'Transportation',	'Num_transfer',	'Time',	'Comfortability',	'Price',	'Walking Distance',	'Acceptable price',	'MTR',	'Bus',	'Shuttle Bus',	'Taxi',	'Tram']
data = data.drop([0, 1], axis = 0)
data = data.iloc[:,18:]
data = data.drop(['Q7_5_TEXT', 'Q7_5','Q5_6_TEXT'], axis= 1)
CA_raw = data.loc[:, 'Q8_1_1': 'Q8_5_6']
data = data.drop(data.loc[:, 'Q8_1_1': 'Q8_5_6'], axis = 1)
data.columns= data_col_name


# drop non-binary gender/ prefer not to say
data = data[(data['Gender']  == '1') | (data['Gender'] == '2')]

# group all responses for over $6000 monthly expense
# Group MTR and non-MTR
# Group more or equal to 3 transfers
data = data.replace({'Monthly Expense': {'4':'3', '5': '3', '6':'3'}, 'Transportation': {'3':'2', '4':'2', '5':'2', '6':'2'}, 'Num_transfer': {'4': '3', '5': '3'}})




CA_raw = CA_raw.fillna(0)
CA_raw = CA_raw.astype(int)
count = CA_raw.sum()
CA = np.zeros((5, 6))

for i, val  in enumerate(count):
    CA[i//6, i%6] = int(val)
CA = pd.DataFrame(CA)
CA.columns = ['Fast', 'Con', 'Seat', 'Transfer', 'Price', 'Walk']
CA.index = ['MTR', 'Bus', 'Shttle', 'Taxi', 'Tram']

data = data.reset_index()
data = data.drop(['index'], axis = 1)
# %%
data.to_csv('data.csv')
CA.to_csv('CA.csv')


# %%
data

# %%
