class Solution {
public:
    int maxProfit(vector<int>& prices) {
        map<int, int> dp;
        int minEl = INT_MAX, maxEl = INT_MIN;
        for(int k = 0; k<2;k++){
            for(int i = 0;i<prices.size();i++){
                minEl = min(prices[i] - dp[i], minEl);
                maxEl = max(maxEl, prices[i]-minEl);
                dp[i] = maxEl;
                // cout<<dp[i]<<"idx: "<<i<<endl;
            }
            minEl = INT_MAX; maxEl = INT_MIN;
        }

        return dp[prices.size()-1];
    }
};