class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n2 > n1:
            return ""
        if s == t:
            return s

        min_s = ""
        l_m = float('inf')
        s_t_counts = {}
        t_counts = {}

        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        def is_all_exist(s_t_counts, t_counts):
            for char, count in t_counts.items():
                if s_t_counts.get(char, 0) < count:
                    return False
            return True

        left = 0
        for right in range(len(s)):
            char = s[right]
            s_t_counts[char] = s_t_counts.get(char, 0) + 1

            while is_all_exist(s_t_counts, t_counts):
                current_window_len = right - left + 1
                if current_window_len < l_m:
                    min_s = s[left:right + 1]
                    l_m = current_window_len

                left_char = s[left]
                s_t_counts[left_char] -= 1
                if s_t_counts[left_char] == 0:
                    del s_t_counts[left_char]
                left += 1

        return min_s