def Factorial(n):
    result = 1
    for i in range(2,n + 1):
        result = result * i
    
    return result

print(Factorial(5))