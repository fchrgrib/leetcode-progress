class Solution {
public:
    int uniquePaths(int m, int n) {
        map<pair<int, int>, int> dp;

        for(int i = n;i>0;i--){
            for(int j = 1;j<=m;j++){
                if(j == 1){
                    dp[{i, j}] = 1;
                    continue;
                }
                int temp1 = dp[{i+1, j}], temp2 = dp[{i, j-1}];
                if(temp1 || temp2) dp[{i,j}] = temp1+temp2;
            }
        }

        return dp[{1, m}];
    }
};