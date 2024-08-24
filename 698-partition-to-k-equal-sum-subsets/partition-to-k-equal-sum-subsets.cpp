class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % k != 0) return false;

    int target = sum / k;
    sort(nums.rbegin(), nums.rend()); 
    vector<int> subsetSums(k, 0);
    
    function<bool(int)> backtrack = [&](int index) {
        if (index == nums.size()) return true;
        
        int num = nums[index];
        for (int i = 0; i < k; i++) {
            if (subsetSums[i] + num <= target) {
                subsetSums[i] += num;
                if (backtrack(index + 1)) return true;
                subsetSums[i] -= num;
            }
            if (subsetSums[i] == 0) break;
        }
        return false;
    };

    return backtrack(0);
}
};