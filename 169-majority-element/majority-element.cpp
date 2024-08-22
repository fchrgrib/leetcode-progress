class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> t;
        int max = INT_MIN;
        for(auto k:nums){
            t[k]++;
            if(t[k]>max) max = t[k];
        }

        for(auto const&k:t){
            if(k.second == max) return k.first;
        }

        return -1;
    }
};