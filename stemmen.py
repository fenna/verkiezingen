import json
import pandas as pd

f = open('out')
data = json.load(f)
cbs = pd.read_csv('Gemeenten.csv', sep = ';', dtype=object)
try:
    Gemeente = cbs[cbs['Gemeentecode']==data['cbsCode']]['Gemeentenaam'].values.tolist()[0]
except:
    Gemeente = data['cbsCode']
df = pd.DataFrame.from_dict(data['parties'])
nu = df['results'][5]['current']['votes']
prev = df['results'][5]['previous']['votes']
print(f'{Gemeente} 2017: {prev} 2021: {nu}')
with open('votes.csv', 'a') as f:
    f.write(f'\n{Gemeente};{prev};{nu}')
