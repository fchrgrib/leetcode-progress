/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let sum = 0;
    while (n != 0){
        sum += n %2;
        n = Math.floor(n/2);
    }

    return sum;
};