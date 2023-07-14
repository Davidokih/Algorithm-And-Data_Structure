const bubble_sort = (seq) => {
    for (i = 0; i < seq.length; i++) {
        for (j = 1; j < seq.length; j++) {
            if (seq[ j ] < seq[ j - 1 ]) {
                let temp = seq[ j ];
                seq[ j ] = seq[ j - 1 ];
                seq[ j - 1 ] = temp;
            }
        }
    }
};

let my_list = [ 1, 8, 5, 2, 0 ];
bubble_sort(my_list);
console.log(my_list);

// Big-O = O(n^2)