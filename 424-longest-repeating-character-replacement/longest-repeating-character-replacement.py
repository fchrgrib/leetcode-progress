class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = len(s)
        if ls == 1:
            return 1
        char_count = [0] * 26
        curr_max = 0
        l = 0
        res = 0

        for i in range(ls):
            curr_el = ord(s[i]) - ord('A')
            char_count[curr_el]+=1
            curr_max = max(curr_max, char_count[curr_el])
            window = i-l+1
            while window - curr_max > k:
                left_idx = ord(s[l]) - ord('A')
                char_count[left_idx] -= 1
                l += 1
                window = i-l+1

            res = max(res, window)

        return res
        