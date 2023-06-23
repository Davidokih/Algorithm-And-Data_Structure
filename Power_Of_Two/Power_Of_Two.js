const Power_Of_Two = (n) => {
    if (n < 1) {
        return false;
    }
    while (n > 1) {
        if (n % 2 !== 0) {
            return false;
        }
        n = n / 2;
    }
    return true;
};

console.log(Power_Of_Two(6));

// Big-O = O(logn)

const isPower_Of_Two = (n) => {
    if (n < 1) {
        return false;
    }
    return (n & (n - 1)) === 0;
};

console.log(isPower_Of_Two(4));

// Big-O = O(1)