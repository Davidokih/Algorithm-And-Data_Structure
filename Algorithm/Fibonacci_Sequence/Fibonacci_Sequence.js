const Fibonacci_Sequence = (n) => {
    const fib = [ 0, 1 ];
    for (i = 2; i < n; i++) {
        fib[ i ] = fib[ i - 1 ] + fib[ i - 2 ];
        // fib.push(fib[ i - 1 ] + fib[ i - 2 ]);
    }
    return fib;
};

console.log(Fibonacci_Sequence(7));

// Big-O = O(n)