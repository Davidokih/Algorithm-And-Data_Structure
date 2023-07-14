def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if(seq[j] > seq[j+1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]

myList = [1,8,5,2,0]
print(myList)
bubble_sort(myList)
print(myList)