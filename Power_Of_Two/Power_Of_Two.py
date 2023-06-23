def Power_Of_Two(n):
    for i in range(11):
        if(2**i == n):
            return True
    return False

print(Power_Of_Two(6))

# Big-O = O(n)

def power_of_two_while(n):
    if(n < 1):
        return False
    while(n > 1):
        if(n % 2 != 0):
            return False
        n = n / 2

    return True

print(power_of_two_while(5))

# Big-O = O(logn)

def power_of_two_bitwise(n):
    if(n < 1):
        return False
    return (n & (n - 1)) == 0

print(power_of_two_bitwise(4))

# Big-O = O(1)