class Solution {
public:
    bool isPalindrome(string s){
        int l = 0, r = s.length()-1;

        while (l<r){
            if (s[l]!=s[r]) return false;
            l++;r--;
        }

        return true;
    }
    vector<vector<string>> partition(string s) {
    int n = s.length();
    vector<vector<vector<string>>> dp(n + 1);

    dp[0] = {{}};

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            string sub = s.substr(j, i - j);
            if (isPalindrome(sub)) {
                for (auto &v : dp[j]) {
                    vector<string> newPartition = v;
                    newPartition.push_back(sub);
                    dp[i].push_back(newPartition);
                }
            }
        }
    }

    return dp[n];
}
};