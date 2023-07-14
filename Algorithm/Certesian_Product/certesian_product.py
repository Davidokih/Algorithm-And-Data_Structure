def certesian_product(arr1,arr2):
    result = []
    for i in arr1:
        for j in arr2:
            result.append([i, j])
    return result

list1 = [1,2]
list2 = [3,4,5]
print(certesian_product(list1, list2))