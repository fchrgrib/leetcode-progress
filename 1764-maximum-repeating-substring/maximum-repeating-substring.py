class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word == sequence:
            return 1
        sum =  0

        for i in range(len(sequence)):
            if sequence[i:i+len(word)] == word:
                tmp = 1
                idx = i+len(word)
                while sequence[idx:idx+len(word)] == word:
                    idx+=len(word)
                    tmp+=1
                sum = max(sum, tmp)

            
        return sum