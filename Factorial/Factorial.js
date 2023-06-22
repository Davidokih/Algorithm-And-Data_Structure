const Factorial = (n) => {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result = result * i;
    }
    return result;
};

console.log(Factorial(0));

// Big-O = O(n)