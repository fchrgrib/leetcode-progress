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
            if (curr_max+k) - window<0:
                while (curr_max+k) - window<0:
                    tmp_el = ord(s[l]) - ord('A')
                    char_count[tmp_el]-=1
                    curr_max = max(char_count)
                    l+=1
                    window = i-l+1

            res = max(res, window)

        return res
        