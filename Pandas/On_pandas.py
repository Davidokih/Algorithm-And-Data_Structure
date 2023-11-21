import pandas as pd
import numpy as np
my_series = pd.Series([10, 27, 32, 41, 5])

"""print("The size of the Series:", my_series.size)

print("The number of dimension of thye Series is:", my_series.ndim)"""
# The head function returns a specified element at the begining of the series:

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue',
         'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]


"""print(my_series.head(2))

print(my_series[2])
print(my_series[2: 4])"""

numbers = [[1, 2, 39, 47, 90], [1, 2, 39, 47, 90]]

# df = pd.DataFrame(numbers)


arr = np.array([[1, 2, 39, 67, 90], [8, 12, 45, 12, 8], [2, 8, 34, 90, 192]])

"""df = pd.DataFrame(arr)
print(df.describe().T)"""


# new_arr = np.random.randint(low=0, high=100, size=20)

# my_arr = new_arr.reshape(4, 5)

# df = pd.DataFrame(my_arr)
# print(df)
last_year = pd.read_csv("employee_revenue_lastyear.csv")

# print(last_year.head(8))
# print(last_year.tail())

last_year["Year"] = 2022

# print(last_year)
dictionary = {
    "name": names,
    "calls": call_numbers,
    "avg_deal_size": average_deal_sizes,
    "revenue": revenues
}

current_year = pd.DataFrame(dictionary)

current_year["Year"] = 2023

# print(current_year.head())

current_year.columns = last_year.columns

all_data = pd.concat([last_year, current_year], axis=0)


# To check if NAN is in the DataFrame
# print(all_data.isna().any())

all_data.fillna(value=np.mean(all_data), inplace=True)

all_data.drop_duplicates(inplace=True)
all_data.reset_index(drop=True, inplace=True)

# print(all_data.describe())
# print(all_data[all_data["Year"] == 2022].describe())
# print(all_data[all_data["Year"] == 2023].describe())

# print(all_data.sort_values(by="Revenue"))

# print(all_data[all_data["Year"] == 2023].sort_values(by="Revenue"))

# print(all_data)

print(all_data["Name"].value_counts())
