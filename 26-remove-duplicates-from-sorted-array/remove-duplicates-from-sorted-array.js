/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let res = 1, init = nums[0];
    for(let i = 1;i<nums.length;i++){
        if (nums[i] !== nums[i - 1]) {
            nums[res] = nums[i]; 
            res++;
        }
    }

    return res;
};