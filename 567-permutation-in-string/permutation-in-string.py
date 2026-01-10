
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False

        need = Counter(s1)
        missing = l1
        left = 0

        for right in range(l2):
            ch = s2[right]

            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if right - left + 1 > l1:
                left_char = s2[left]
                if need[left_char] >= 0:
                    missing += 1
                need[left_char] += 1
                left += 1

            if missing == 0:
                return True

        return False
        

        