class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        counter = Counter(s)
        
        for c in counter:
            if counter[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        
        return len(s)
        