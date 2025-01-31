class Solution {
public:
    int change(int amount, vector<int>& coins) {
        map<pair<int, int>, unsigned int> dp;
        try{
            for(int i = coins.size()-1;i>=0;i--){
                for(int j = 0;j<=amount;j++){
                    if(j == 0){
                        dp[{coins[i], j}] = 1;
                        continue;
                    }
                    unsigned int temp1 = (i+1<coins.size())?dp[{coins[i+1], j}]:0;
                    unsigned int temp2 = (j-coins[i]>=0)?dp[{coins[i], j - coins[i]}]:0;
                    if( temp1 || temp2 ) dp[{coins[i], j}] = temp1 + temp2;
                }
            }
        } catch (out_of_range& e){}
        

        return dp[{coins[0], amount}];
    }
};