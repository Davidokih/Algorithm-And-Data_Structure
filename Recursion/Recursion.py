import math

def recursive_fibonacci(n):
    if(n < 2):
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# print(recursive_fibonacci(6))

# Big-O = O(2^n)

def recursive_factorial(n):
    if(n == 0):
        return 1
    return n * recursive_factorial(n - 1)

# print(recursive_factorial(5))

# Big-O = O(n)

def recursive_binary_search(arr,target):
    return search(arr, target, 0, len(arr) - 1)

def search(arr, target, leftIndex, rightIndex):
    if(leftIndex > rightIndex):
        return -1
    
    middleIndex = math.floor((leftIndex + rightIndex) / 2)
    if(target == arr[middleIndex]):
        return middleIndex
    if(target < arr[middleIndex]):
        return search(arr, target, leftIndex, middleIndex - 1)
    else:
        return search(arr, target, middleIndex + 1, rightIndex)

print(recursive_binary_search([ -5, 2, 4, 6, 18 ], 6))

# Big-O = O(logn)