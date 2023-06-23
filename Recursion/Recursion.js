const recursive_fibonacci = (n) => {
    if (n < 2) {
        return n;
    }
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
};

console.log(recursive_fibonacci(6));

// Big-O = O(2^n)

const recursive_factorial = (n) => {
    if (n === 0) {
        return 1;
    }
    return n * recursive_factorial(n - 1);
};

console.log(recursive_factorial(5));

// Big-O = O(n)