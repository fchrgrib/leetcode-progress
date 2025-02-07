class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, r = 0, maxEl = INT_MIN, flip = k;
        while(r<nums.size()){
            if(!flip && !nums[r]){
                if(!nums[l]){
                    l++;
                }else{
                    while(nums[l] != 0 && l<r) {l++;}
                    l++;
                }
            }
            if(!nums[r] && flip>0) flip--;
            maxEl = max(maxEl, (r-l)+1);
            // cout<<l<<r<<flip<<endl;
            // cout<<"max: "<<maxEl<<endl;
            r++;
            
        }
        return maxEl;
    }
};