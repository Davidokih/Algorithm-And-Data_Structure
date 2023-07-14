const insertion_sort = (arr) => {
    for (i = 1; i < arr.length; i++) {
        let number_to_insert = arr[ i ];
        let j = i - 1;
        while (j >= 0 && arr[ j ] > number_to_insert) {
            arr[ j + 1 ] = arr[ j ];
            j = j - 1;
        }
        arr[ j + 1 ] = number_to_insert;
    }
};
const my_list = [ 8, 20, -2, 4, -6 ];
insertion_sort(my_list);
console.log(my_list);

// Big-O = O(n^2)