class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int idx = 0;
        map<int,int> memo;

        for(int t: nums){
            if(memo[t]>=2) continue;
            nums[idx] = t;
            memo[t]++;idx++;
        }

        // cout<<idx<<endl;

        return idx;
    }
};