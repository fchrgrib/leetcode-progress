class Solution {
public:
    vector<vector<int>> res;
    map<vector<int>, bool> isExists;
    void bc(int check, vector<int> nums, vector<int> temp){
        if (check>=nums.size()) return;

        if (temp[temp.size()-1]<=nums[check]){
            temp.push_back(nums[check]);
            if (!isExists[temp]) {res.push_back(temp);isExists[temp]=true;}
            bc(check+1, nums, temp);
            temp.pop_back();
            bc(check+1, nums, temp);
        }else{
             bc(check+1, nums, temp);
        }
    }
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        for(int i = 0;i<(nums.size()-1);i++) bc(i+1,nums,{nums[i]});
        return res;
    }
};