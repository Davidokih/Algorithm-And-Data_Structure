
const climbing_staircase = (n) => {
    const noOfWays = [ 1, 2 ];
    for (i = 2; i <= n; i++) {
        noOfWays[ i ] = noOfWays[ i - 1 ] + noOfWays[ i - 2 ];
    }
    return noOfWays[ n - 1 ];
};

console.log(climbing_staircase(4));
// Big-O = O(n)