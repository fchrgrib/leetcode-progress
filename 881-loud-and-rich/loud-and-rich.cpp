class Solution {
public:
    map<int, vector<int>> temp;
    map<int, int> dp;  
    vector<int> res;

    void init(vector<vector<int>>& richer, int size, vector<int>& quiet) {
        for (const auto& t : richer) temp[t[1]].push_back(t[0]);

        res.resize(size, -1);
        for (int i = 0; i < size; i++) {
            res[i] = findQuietest(i, quiet); 
        }
    }

    int findQuietest(int person, vector<int>& quiet) {
        if (dp.find(person) != dp.end()) return dp[person];  

        int minQuiet = quiet[person];  
        int quietestPerson = person;   

        for (int richerPerson : temp[person]) {
            int candidate = findQuietest(richerPerson, quiet);  
            if (quiet[candidate] < minQuiet) {
                minQuiet = quiet[candidate];
                quietestPerson = candidate;
            }
        }

        dp[person] = quietestPerson;  
        return quietestPerson;
    }

    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        init(richer, quiet.size(), quiet);
        return res;
    }
};