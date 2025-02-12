/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let l1 = s.length, l2 = p.length;
    let dp = Array.from({ length: l1 }, () => new Array(l2).fill(-1));

    const sl = (idx1, idx2) => {
        if(idx1>=l1 && idx2>=l2){
            return true;
        }
        if(idx1<l1 && idx2<l2 && dp[idx1][idx2] != -1) return dp[idx1][idx2];

        if((l1 - idx1) == 0 && p[idx2] != "*") return false;
        if((l2 - idx2) == 0 && s[idx1] != "*") return false;

        
        if(s[idx1] === "*" || p[idx2] === "*"){
            let t = false;
            t |= (idx1<l1) ? sl(idx1+1, idx2): false;
            t |= (idx2<l2) ? sl(idx1, idx2+1): false;
            t |= (idx1<l1 && idx2<l2) ? sl(idx1+1, idx2+1): false;
            if(idx1<l1 && idx2<l2) dp[idx1][idx2] = t;
            return t;
        }

        if(
            s[idx1] === p[idx2] ||
            (s[idx1] == "?" && p[idx2] != "") ||
            (p[idx2] == "?" && s[idx1] != "")){
                dp[idx1][idx2] = sl(idx1+1, idx2+1);
            return dp[idx1][idx2];
        }

        if(idx1<l1 && idx2<l2) dp[idx1][idx2] = false;

        return false;
    }


    return sl(0,0);
};