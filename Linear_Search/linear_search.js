const linear_search = (arr, target) => {
    for (i = 0; i < arr.length; i++) {
        if (arr[ i ] === target) {
            return i;
        }
    }
    return -1;
};

console.log(linear_search([ -5, 2, 18, 4, 6 ], 18));

// Big-O = O(n)