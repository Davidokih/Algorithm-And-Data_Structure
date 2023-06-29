import math
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
           if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

my_list = [ 8, 20, -2, 4, -6 ]
insertion_sort(my_list)
print(my_list)