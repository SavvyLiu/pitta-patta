import pandas as pd
df = pd.read_csv('carib_dataset.csv')
df['prompt'] = df['prompt'].str.slice(4)

df.to_json('carib_dataset.json', orient='records')