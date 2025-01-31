class Solution {
public:
    void bc(int eL, vector<int>& nums, int target, int& sum){
        if(eL == 0 && target == 0){
            sum++;
            return;
        }

        if(eL>0) {bc(eL-1, nums, target - nums[eL-1], sum);
        bc(eL-1, nums, target + nums[eL-1], sum);}
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        bc(nums.size(), nums, target, sum);
        return sum;
    }
};