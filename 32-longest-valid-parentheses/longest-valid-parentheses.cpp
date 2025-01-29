class Solution {
public:
    int longestValidParentheses(string s) {
        stack<pair<char, int>> temp;
        map<int, int> dp;
        int maxEl = 0;

        for(int i = 0;i<s.size();i++){
            if(s[i] == ')' && !temp.empty()){
                auto& t = temp.top();

                if(t.first == '('){
                    dp[i]+=(dp[t.second - 1]+(i-t.second+1));
                    maxEl = max(dp[i], maxEl);
                }
                temp.pop();
                continue;
            }
            
            temp.push({s[i], i});
        }
        
        return maxEl;
    }
};