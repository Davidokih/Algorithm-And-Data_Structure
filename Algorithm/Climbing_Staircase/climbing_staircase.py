def climbing_staircase(n):
    num_of_ways = [1,2]
    for i in range(2, n):
        num_of_ways.append(num_of_ways[i - 1] + num_of_ways[i-2])
    return num_of_ways[n -1]

print(climbing_staircase(5))