/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    const max_el = Math.max(...strs.map((a) => a.length));
    let res = "";
    for(let i = 0;i<max_el;i++){
        const is_same = strs.every((s) => s[i] === strs[0][i])
        if (!is_same) break;
        res+=strs[0][i]
    }

    return res
};