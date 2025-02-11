class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxEl = INT_MIN, sum = 0;
        for(auto& t: nums){
            sum+=t;maxEl = max(maxEl, sum);
            if(sum<0){
                sum = 0;continue;
            }
            
        }

        return maxEl;
    }
};