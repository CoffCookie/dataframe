import sys
import pandas as pd 

args = sys.argv
file_name = args[1]

print(file_name)
print(type(file_name))

anime_datalist = pd.read_csv(file_name)
print(anime_datalist.head())

print(anime_datalist.columns)

row_count = 0
all_row_num = len(anime_datalist)
print(all_row_num)

print(anime_datalist['Title'][1])

while row_count < 50:
    print(anime_datalist['Title'][row_count])
    row_count = row_count + 1