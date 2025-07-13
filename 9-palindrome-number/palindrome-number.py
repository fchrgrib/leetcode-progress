class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        l = len(tmp)
        h = l//2
        if tmp[0] == '-':
            return False

        if l == 1:
            return True

        for i in range(h):
            if tmp[i] != tmp[l-i-1]:
                return False

        return True