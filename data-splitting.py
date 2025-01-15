import pandas as pd
df = pd.read_csv('/Users/aak/Desktop/tablo_verileri.csv')
yil_values = [2023, 2022, 2021]

for yil in yil_values:
    df_yil = df[df['Yıl'] == yil]
    df_yil.to_csv(f'/Users/aak/Desktop/tekno_fest_{yil}.csv', index=False)
