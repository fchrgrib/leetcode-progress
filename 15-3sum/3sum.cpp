class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int l = 0, r = nums.size()-1, m = 0, size = nums.size(), temp = 0;
        set<vector<int>> res;
        vector<vector<int>> resA;
        sort(nums.begin(), nums.end());

        for(int i = 0;i<size-2;i++){
            if(nums[i]>0) break;
            l=i+1;r=size-1;
            while (l<r){
                temp = nums[i]+nums[l]+nums[r];
                if(temp == 0){
                    res.insert({nums[i],nums[l],nums[r]});
                    l++;
                }else if(temp>0) r--; else l++;
            }
        }

        for(auto& t:res) resA.push_back(t);

        return resA;
    }
};