class Solution:
    def largestNumber(self, nums):
        strs = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0

        strs.sort(key=cmp_to_key(compare))

        result = "".join(strs)

        return "0" if result[0] == "0" else result