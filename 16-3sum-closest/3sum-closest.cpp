class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1, res = 0, size = nums.size(), m = 0, min = INT_MAX;
        sort(nums.begin(), nums.end());

        for(int i = 0;i<size-2;i++){
            l=i+1;r=size-1;
            while(l<r){
                int temp = nums[i] + nums[l] + nums[r];
                if(temp == target){
                    res = temp;break;
                }else if(temp>target) r--; else l++;

                int msr = abs(target-temp);
                if(msr<min){
                    min = msr;res=temp;
                }
            }
        }

        return res;
    }
};