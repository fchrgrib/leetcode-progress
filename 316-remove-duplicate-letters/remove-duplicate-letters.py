class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        letter_used = []
        last_letter = {}

        for i in range(len(s)):
            last_letter[s[i]] = i

        for i in range(len(s)):
            if s[i] in letter_used:
                continue
            

            while len(res)>0 and res[-1]>s[i] and i < last_letter[res[-1]]:
                letter_used.remove(res.pop())
            res.append(s[i])
            letter_used.append(s[i])

        

        return "".join(res)
        