const certesian_product = (arr1, arr2) => {
    const ressult = [];
    for (i = 0; i < arr1.length; i++) {
        for (j = 0; j < arr2.length; j++) {
            ressult.push([ arr1[ i ], arr2[ j ] ]);
        }
    }
    return ressult;
};

const list1 = [ 1, 2 ];
const list2 = [ 3, 4 ];
console.log(certesian_product(list1, list2));

// Big-O = O(mn)