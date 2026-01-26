class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        if nums[0] == target:
            return True
        for i in range(1, len(nums)):
            if nums[i] == target:
                return True
            if nums[i]<nums[i-1]:
                start = i
                break
        
        end = len(nums)-1
        while start<=end:
            m = (start+end)//2
            if nums[m] == target:
                return True
            if nums[m]<target:
                start = m+1
            else:
                end = m-1
        return False