class Solution {
public:
    int rob(vector<int>& nums) {
        map<int, int> memo;
        int maxEl = INT_MIN;

        for(int i = nums.size()-1;i>=0;i--){
            if(i == nums.size()-1){
                memo[i] = nums[i];
                maxEl = nums[i];
                continue;
            }
            memo[i] = max({nums[i], nums[i]+memo[i+1]-nums[i+1], nums[i]+memo[i+2]});
            maxEl = max(memo[i], maxEl);
        }
        return maxEl;
    }
};