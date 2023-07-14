const marge_sort = (arr) => {
    if (arr.length < 2) {
        return arr;
    }
    const mid = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, mid);
    const rightArr = arr.slice(mid);
    return marge(marge_sort(leftArr), marge_sort(rightArr));
};

const marge = (leftArr, rightArr) => {
    const sortedArr = [];
    while (leftArr.length && rightArr.length) {
        if (leftArr[ 0 ] <= rightArr[ 0 ]) {
            sortedArr.push(leftArr.shift());
        } else {
            sortedArr.push(rightArr.shift());
        }
    }
    return [ ...sortedArr, ...leftArr, ...rightArr ];
};

my_list = [ 8, 20, -2, 4, -6 ];

console.log(marge_sort(my_list));

// Big-O = O(nlogn)