class Solution {
public:
    int findSubstringInWraproundString(string s) {
        vector<int> alphabet(26,0);
        int len = 0, currentLength = 0;

        for(int i =0;i<s.size();i++){
            if(i>0 &&(s[i] - s[i-1] == 1 || s[i] - s[i-1] == -25)) currentLength++; else currentLength = 1;
            int index = s[i] - 'a';
            alphabet[index] = max(alphabet[index], currentLength);
        }

        for(int i:alphabet) len+=i;
        

        return len;
    }
};