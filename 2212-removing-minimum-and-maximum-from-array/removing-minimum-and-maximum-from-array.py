class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = 0
        max_idx = 0
        ln = len(nums)

        for i in range(1, ln):
            if nums[min_idx]>nums[i]:
                min_idx = i
            
            if nums[max_idx]<nums[i]:
                max_idx = i
        
        if max_idx>min_idx:
            return min(max_idx+1, min_idx+1+ln-max_idx, ln-min_idx)
        return min(min_idx+1, max_idx+1+ln-min_idx, ln-max_idx)
        