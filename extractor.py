import pandas as pd 
from shutil import copy2

# Pandas setup
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000) 
pd.set_option('display.max_colwidth', -1) 

# Custom NA dictionary
null_dict = [
  "", 
  "#N/A", 
  "#N/A N/A", 
  "#NA", "-1.#IND", 
  "-1.#QNAN", 
  "-NaN", 
  "-nan", 
  "1.#IND", 
  "1.#QNAN", 
  "<NA>", 
  "N/A", 
  "NA", 
  "NULL", 
  "NaN", 
  "n/a", 
  "nan", 
  "null", 
  "*", 
  "**", 
  "n.d.", 
  "-", 
  "#DIV/0!", 
  "#DIV/0", 
  " ", 
  "\xad", 
  "n.d", 
  "ND", 
  "N.D.", 
  "N.D"
]

# Read file
filename = 'file_name'
field = "field_name"
xls = pd.ExcelFile(f'./raw_data/{filename}.xls')
df = pd.read_excel(
  xls, 
  field, 
  header=2, 
  usecols="A:K", 
  skipfooter=12, 
  na_values=null_dict
)

# Clean data
aux = df.T.reset_index()
colnames = aux.iloc[0, :].tolist()
aux.columns = colnames
aux.drop(labels=[0, 1], axis=0, inplace=True)
aux.drop(aux.tail(2).index, inplace=True)
df = aux
# name = df.iloc[0,0]
# rename = [name for value in df[df.columns[0]].values]
# df[df.columns[0]] = rename
df['Data'] = df['Data'].astype('datetime64')
repr(df)

# Save as csv
field = field.replace(" ", "_")
field = field.lower()
year = filename.split()[-1:][0].split(".")[0]
df.to_csv(f"./Dataset/{field}_{year}.csv", encoding='utf8', index=False)
