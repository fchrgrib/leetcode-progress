/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let sum = 0;
    let l = digits.length;

    for (let i = l-1;i>=0;i--){
        if(digits[i] === 9){
            digits[i] = 0;
            sum = 1
        }else{
            digits[i]++;
            sum = 0
        }

        if(sum === 0 ) break
    }
    

    if (digits[0] === 0){
        digits.unshift(1)
    }
    return digits
};