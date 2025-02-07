class Solution {
public:
    int maxVowels(string s, int k) {
        map<char, bool> t;
        t['a']=true;t['i']=true;t['u']=true;t['e']=true;t['o']=true;
        int sum = 0, maxEl = 0;
        for(int i = 0;i<s.size();i++){
            if(t[s[i]]) sum++;
            if(i>=k && t[s[i-k]]) sum--;
            maxEl = max(maxEl, sum);
        }

        return maxEl;
    }
};