const binary_search = (arr, target) => {
    // let arr = array.sort((a, b) => a - b);
    let leftIndex = 0;
    let rightIndex = arr.length - 1;

    while (leftIndex < rightIndex) {
        let middleIndex = Math.floor((leftIndex + rightIndex) / 2);
        if (arr[ middleIndex ] === target) {
            return middleIndex;
        }
        if (target < arr[ middleIndex ]) {
            rightIndex = middleIndex - 1;
        } else {
            leftIndex = middleIndex + 1;
        }
    }
    return -1;
};

console.log(binary_search([ -5, 2, 4, 6, 18 ], 2));

// Big-O = O(logn)