import pandas as pd

data = {
    'Набор A' : [85, 90, 95, 100, 105],
    'Набор B' : [70, 80, 95, 110, 120]
}
df = pd.DataFrame(data)

stda = df['Набор A'].std()
stdb = df['Набор B'].std()

print(f'Стандартное отклонение набор А : {stda}')
print(f'Стандартное отклонение набор B : {stdb}')