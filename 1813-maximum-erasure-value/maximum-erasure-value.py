class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ln = len(nums)
        pref_sum = [0] * (ln+1)
        prefix_sum = 0
        el_idx = {}
        res, l = 0, 0

        for i in range(ln):
            prefix_sum+=nums[i]
            pref_sum[i+1] = prefix_sum

            if nums[i] in el_idx:
                l = max(el_idx[nums[i]] + 1,l)
            el_idx[nums[i]] = i
            res = max(prefix_sum-pref_sum[l], res)
        return res



        