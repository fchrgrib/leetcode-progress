/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = "";

    for (let i = 0; i < strs[0].length; i++) {
        if (strs.some(s => s[i] !== strs[0][i])) break;
        prefix += strs[0][i];
    }

    return prefix;
};