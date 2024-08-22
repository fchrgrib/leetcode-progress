class Solution {
public:
    vector<vector<int>> res;
    void bc(int start, vector<int> nums, vector<int> tmp){
        if (start == nums.size()) return;
        tmp.push_back(nums[start]);
        res.push_back(tmp);
        for(int i = start;i<nums.size();i++) bc(i+1, nums, tmp);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        res.push_back({});
        if(nums.empty()) return res;
        
        for(int i = 0;i < nums.size();i++) bc(i, nums, {});
        return res;
    }
};