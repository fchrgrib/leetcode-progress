class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(''.join(reversed(s)).split(" ")))