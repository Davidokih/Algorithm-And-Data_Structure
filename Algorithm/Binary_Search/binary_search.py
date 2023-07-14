import math

def binary_search(arey, target):
    arr = sorted(arey)
    leftIndex = 0
    rightIndex = len(arr) - 1

    while(leftIndex <= rightIndex):
        middleIndex = math.floor((leftIndex + rightIndex) / 2)
        if(target == arr[middleIndex]):
            return middleIndex
        if(target < arr[middleIndex]):
            rightIndex = middleIndex - 1
        else:
            leftIndex = middleIndex + 1
    return -1

print(binary_search([ -5, 2, 18, 4, 6 ], 6))

# Big-O = O(logn)

# print(sorted([ -5, 2, 18, 4, 6 ]))