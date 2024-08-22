class Solution {
public:
    vector<vector<string>> alphabetNum={
            {},
            {"a","b","c"},
            {"d","e","f"},
            {"g", "h", "i"},
            {"j", "k", "l"},
            {"m", "n", "o"},
            {"p", "q", "r", "s"},
            {"t", "u", "v"},
            {"w", "x", "y","z"}
    };
    vector<string> res;
    
    void bc(int start,vector<int> nums, string tmp){
        if (tmp.length() == nums.size()){
            res.push_back(tmp);
            return;
        }
        
        for(int i = 0; i<alphabetNum[nums[start]].size(); i++) 
            bc(start+1, nums, tmp+alphabetNum[nums[start]][i]);
    }
    vector<string> letterCombinations(string digits) {
        if (!digits.length()) return {};
        vector<int> t;
        for(auto i: digits) t.push_back((i - '0')-1);
        bc(0, t, "");
        return res;
    }
};