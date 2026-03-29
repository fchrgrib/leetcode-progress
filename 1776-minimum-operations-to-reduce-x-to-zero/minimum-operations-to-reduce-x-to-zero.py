class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        prefix = 0
        pos = {0: -1}
        max_len = -1

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - target in pos:
                max_len = max(max_len, i - pos[prefix - target])

            if prefix not in pos:
                pos[prefix] = i

        return len(nums) - max_len if max_len != -1 else -1