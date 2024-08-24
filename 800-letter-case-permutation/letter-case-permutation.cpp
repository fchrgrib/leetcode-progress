class Solution {
public:
    string s;
    vector<string> res;
    string ans = "";

    void solve(int x) {
        if (x == s.size()) {
            res.push_back(ans);
            // cout << ans << endl;
            return;
        }

        if ((s[x] >= 'A' && s[x] <= 'Z') || (s[x] >= 'a' && s[x] <= 'z')) {
            ans.push_back(tolower(s[x]));
            solve(x+1);
            ans.pop_back();

            ans.push_back(toupper(s[x]));
            solve(x+1);
            ans.pop_back();
        } else {
            ans.push_back(s[x]);
            solve(x+1);
            ans.pop_back();
        }
    }

    vector<string> letterCasePermutation(string s) {
        this->s = s;

        solve(0);
        return res;
    }

};