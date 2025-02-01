class Solution {
public:
    int slW(int w1, int w2, string& word1, string& word2, vector<vector<int>>& memo) {
        // Base cases
        if (w1 == word1.size()) {
            return word2.size() - w2;  // Insert remaining characters of word2
        }
        if (w2 == word2.size()) {
            return word1.size() - w1;  // Delete remaining characters of word1
        }

        // Check if the result is already computed
        if (memo[w1][w2] != -1) {
            return memo[w1][w2];
        }

        // If characters match, move to the next characters
        if (word1[w1] == word2[w2]) {
            memo[w1][w2] = slW(w1 + 1, w2 + 1, word1, word2, memo);
        } else {
            // Try all three operations: insert, delete, replace
            int insert = slW(w1, w2 + 1, word1, word2, memo);
            int del = slW(w1 + 1, w2, word1, word2, memo);
            int replace = slW(w1 + 1, w2 + 1, word1, word2, memo);
            memo[w1][w2] = 1 + min({insert, del, replace});
        }

        return memo[w1][w2];
    }

    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        // Memoization table initialized with -1
        vector<vector<int>> memo(m, vector<int>(n, -1));

        return slW(0, 0, word1, word2, memo);
    }
};