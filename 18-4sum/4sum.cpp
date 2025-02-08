class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1, size = nums.size();
        set<vector<int>> res;
        sort(nums.begin(), nums.end());

        for(int i = 0;i<size-3;i++){
            for(int j = size-1;j>=i+3;j--){
                l=i+1;r=j-1;
                while(l<r){
                    long temp = static_cast<long>(nums[i]) + static_cast<long>(nums[l]) + static_cast<long>(nums[r]) + static_cast<long>(nums[j]);
                    if(temp == static_cast<long>(target)){
                        res.insert({nums[i] , nums[l] , nums[r] , nums[j]});l++;
                    } else if(temp>target) r--; else l++;
                }
            }
        }

        vector<vector<int>> result(res.begin(), res.end());
        return result;
    }
};