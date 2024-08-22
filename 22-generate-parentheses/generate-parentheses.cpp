class Solution {
public:
    vector<string> res;
    void bc(pair<queue<string>,queue<string>> memo, string val, int p){
        if (memo.first.empty() && memo.second.empty()){
            res.push_back(val);
            return;
        }

        if (!memo.first.empty()){
            auto t = memo;
            string tmp = t.first.front();
            t.first.pop();
            bc(t, val+tmp, p+1);
        }
        if (!memo.second.empty() && p>0){
            auto t = memo;
            string tmp = t.second.front();
            t.second.pop();
            bc(t, val+tmp, p-1);
        }
    }
    vector<string> generateParenthesis(int n) {
        pair<queue<string>,queue<string>> memo;
        for(int i = 0;i<n;i++){
            memo.first.push("(");
            memo.second.push(")");
        }
        string val = memo.first.front();
        memo.first.pop();
        bc(memo, val,1);
        return res;
    }
};