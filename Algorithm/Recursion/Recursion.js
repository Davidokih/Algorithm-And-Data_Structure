const recursive_fibonacci = (n) => {
    if (n < 2) {
        return n;
    }
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
};

// console.log(recursive_fibonacci(6));

// Big-O = O(2^n)

const recursive_factorial = (n) => {
    if (n === 0) {
        return 1;
    }
    return n * recursive_factorial(n - 1);
};

// console.log(recursive_factorial(5));

// Big-O = O(n)

const recursive_binary_search = (arr, target) => {
    return search(arr, target, 0, arr.length - 1);
};

const search = (arr, target, leftIndex, rightIndex) => {
    if (leftIndex > rightIndex)
        return -1;

    let middleIndex = Math.floor((leftIndex + rightIndex) / 2);
    if (target === arr[ middleIndex ]) {
        return middleIndex;
    }
    if (target < arr[ middleIndex ]) {
        return search(arr, target, leftIndex, middleIndex - 1);
    }
    else {
        return search(arr, target, middleIndex + 1, rightIndex);
    }
};

console.log(recursive_binary_search([ -5, 2, 4, 6, 18 ], 6));

// Big-O = O(logn)