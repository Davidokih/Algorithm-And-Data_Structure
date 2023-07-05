import math

def sort(arr):
    if(len(arr) <= 1):
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for item in arr:
        if(item > pivot):
            right.append(item)
        else:
            left.append(item)
    return sort(left) + [pivot] + sort(right)
            
my_list = [ 8, 20, -2, 4, -6 ]

print(sort(my_list))

square_list2 = [num for num in my_list]
# print(square_list2)
