class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size() == 1) return true;
        unordered_map<int, bool> val;
        int lastIdx = nums.size()-1;
        for(int i = nums.size() -2;i>=0;i--){
            for(int j = 1;j<=nums[i];j++){
                if(i+j>=lastIdx || val[i+j]){
                    val[i] = true;
                    break;
                }else{
                    val[i] = false;
                }
            }
        }
        return val[0];
    }
};