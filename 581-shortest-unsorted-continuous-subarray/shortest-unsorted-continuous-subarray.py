class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -2 
        
        max_so_far = nums[0]
        for i in range(1, n):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_so_far:
                end = i
        
        min_so_far = nums[-1]
        for i in range(n-2, -1, -1):
            min_so_far = min(min_so_far, nums[i])
            if nums[i] > min_so_far:
                start = i
        
        return end - start + 1