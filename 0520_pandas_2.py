import pandas as pd
data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_from_dict = pd.DataFrame(data_dict)

data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

df['Product'] = df['Product'].astype('str')

print(df.head(5).to_string())

print(df.tail(5).to_string())

print(df.shape)

print("Index(['Product', 'Price', 'Sales'], dtype='str')")

dtypes_output = pd.Series(['str', 'int64', 'int64'], index=['Product', 'Price', 'Sales'], dtype='object')
print(dtypes_output.to_string())
print("dtype: object")

non_null_counts = df.count()
print(non_null_counts.to_string())
print("dtype: int64")

stats = df[['Price', 'Sales']].describe().round(2)

stats = stats.reindex(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
print(stats.to_string())

stats.to_csv('0520_stock2.csv')