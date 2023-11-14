import numpy as np
import time

revenue = [1000, 2000, 3000, 4000, 5000, 6000]

arr = np.array(revenue)

initial_time = time.time()
sum = arr.sum()

# print(sum)
termination_time = time.time()

# print("Execution Time", termination_time - initial_time)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)

# The ndim method is to check number of dimension of tbhe numpy array
# print(arr2.ndim)

# The shape method is to check the number of element in each row and column
# print(arr2.shape)

# The size method is to calculate the number of values in the numpay array
# print(arr2.size)

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue',
         'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

data = np.array([], dtype=int)


def append_names(names_list):
    global data
    for i in names_list:
        data = np.append(data, names.index(i))


def append_performance_measures(feature_list):
    global data
    data = np.append(data, feature_list)


append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

# The reshape method change the array into any specified dimentional array
data = data.reshape(4, 11)

# print(data)

# print(data[0])
# print(data[3, 7])


def calculate_performance(employee_name):
    idx = names.index(employee_name)
    number_of_calls = data[1, idx]
    average_deal_sizes = data[2, idx]
    revenues = data[3, idx]

    score = (average_deal_sizes*revenues)/number_of_calls

    return score


perfprmance_score = []
for name in names:
    score = int(calculate_performance(name))
    perfprmance_score.append(score)
# print(data[1, 4])

data = np.concatenate((data, [perfprmance_score]), axis=0)

# print(data)
print(data.shape)


idx_best_employee = np.argmax(data[4])
idx_worst_employee = np.argmin([4])

print(f'Best Performing Employee {names[idx_best_employee]}')
print(f'Worst Perfoming Employee {names[idx_worst_employee]}')
