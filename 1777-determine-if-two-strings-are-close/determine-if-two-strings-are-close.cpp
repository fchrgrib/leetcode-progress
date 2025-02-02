class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) return false;

        map<char, int> temp1, temp2;
        priority_queue<int> pq1,pq2;
        for(int i = 0; i< word1.size(); i++){
            temp1[word1[i]]++;
            temp2[word2[i]]++;
        }
        for(int i = 0; i< word1.size(); i++){
            if(!temp1[word2[i]] || !temp2[word1[i]]) return false;
            pq1.push(temp1[word1[i]]);
            pq2.push(temp2[word2[i]]);
        }

        if (pq1.size() != pq2.size()) return false;

        while (!pq1.empty() && !pq2.empty()){
            if(pq1.top() != pq2.top()) return false;
            pq1.pop(); pq2.pop();
        }

        return true;
    }
};