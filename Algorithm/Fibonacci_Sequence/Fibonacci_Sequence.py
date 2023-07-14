def Fibonacci_Sequence(n):
    fib = [0, 1]
    for i in range(2,n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

print(Fibonacci_Sequence(7))

# fib = [0, 1]
# for i in range(2,5):
#     print(f"hellow {i}")
# fib.append(2)

# print(fib)

