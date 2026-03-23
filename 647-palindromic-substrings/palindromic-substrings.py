class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        ln = len(s)

        def count_palindrome(i, j):
            while i>=0 and j<ln:
                if s[i] != s[j]:
                    break
                self.res+=1
                i-=1
                j+=1
        
        for i in range(ln):
            count_palindrome(i, i)
            count_palindrome(i, i+1)
        return self.res


        