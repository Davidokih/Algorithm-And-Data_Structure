def quick_sort(arr):
    if(len(arr) <= 1):
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for items in arr:
        if(items > pivot):
            right.append(items)
        else:
            left.append(items)

    return quick_sort(left) + [pivot] + quick_sort(right)

my_list = [ 8, 20, -2, 4, -6 ]
print(quick_sort(my_list))
