class Solution {
public:
    unordered_map<int, bool> dp;
    bool bc(int idx, int size, int prevIdx, vector<int>& arr){
        if(idx<0 || idx>=size) return false;
        if(arr[idx] == 0) return true;
        if(dp.find(idx) != dp.end()) return dp[idx];

        if(idx+arr[idx] != prevIdx){
            dp[idx] |= bc(idx+arr[idx], size, idx, arr);
        }
        
        if(idx-arr[idx] != prevIdx){
            dp[idx] |= bc(idx-arr[idx], size, idx, arr);
        }
        

        return dp[idx];
    }
    bool canReach(vector<int>& arr, int start) {
        return bc(start, arr.size(), -1, arr);
    }
};