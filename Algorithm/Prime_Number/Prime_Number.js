const Prime_Number = (n) => {
    if (n < 2) {
        return false;
    }
    for (i = 2; i < n; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
};

console.log(Prime_Number(113));
// Big-O = O(n)

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    for (i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
};

console.log(isPrime(100));

// Big-O = O(n**2)