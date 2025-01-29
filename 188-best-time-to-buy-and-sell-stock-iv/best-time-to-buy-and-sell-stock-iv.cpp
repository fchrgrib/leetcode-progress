class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        map<int, int> dp;
        int minEl = INT_MAX, maxEl = INT_MIN;
        for(int j = 0; j<k;j++){
            for(int i = 0;i<prices.size();i++){
                minEl = min(prices[i] - dp[i], minEl);
                maxEl = max(maxEl, prices[i]-minEl);
                dp[i] = maxEl;
            }
            minEl = INT_MAX; maxEl = INT_MIN;
        }

        return dp[prices.size()-1];
    }
};