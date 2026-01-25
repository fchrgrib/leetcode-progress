class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        min_nums = float("inf")
        for i in range(len(nums)):
            if i+k-1>=len(nums):
                break
            min_nums = min(min_nums, nums[i]-nums[i+k-1])

        return min_nums if min_nums != float("inf") else 0
        