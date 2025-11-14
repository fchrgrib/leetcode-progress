/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const tmp = s.toLowerCase().replaceAll(/[^a-z0-9]/g,"");
    if (tmp === "") return true;

    const l = tmp.length - 1;
    for (let i = 0;i<l/2;i++){
        if(tmp[i] !== tmp[l-i]) return false
    }

    return true
};