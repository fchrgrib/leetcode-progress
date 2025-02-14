class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        l = len(word) - numFriends + 1
        maxS = ""
        print(l)

        for i in range(len(word)):
            maxS = max(maxS, word[i:i+l])
        
        return maxS