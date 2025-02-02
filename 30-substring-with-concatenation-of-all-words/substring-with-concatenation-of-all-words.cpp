
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if (s.empty() || words.empty()) return res;

        int wordLength = words[0].size();
        int totalWords = words.size();
        int totalLength = wordLength * totalWords;

        if (s.size() < totalLength) return res;

        // Create a frequency map for words
        unordered_map<string, int> wordCount;
        for (const string& word : words) {
            wordCount[word]++;
        }

        
        for (int i = 0; i < wordLength; ++i) {
            int left = i; 
            int right = i; 
            unordered_map<string, int> seenWords; 
            int count = 0;

     
            while (right + wordLength <= s.size()) {
                string word = s.substr(right, wordLength);
                right += wordLength;

               
                if (wordCount.find(word) != wordCount.end()) {
                    seenWords[word]++;
                    count++;

                    
                    while (seenWords[word] > wordCount[word]) {
                        string leftWord = s.substr(left, wordLength);
                        seenWords[leftWord]--;
                        count--;
                        left += wordLength;
                    }

                    if (count == totalWords) {
                        res.push_back(left);
                    }
                } else {
                    seenWords.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return res;
    }
};