class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum_int = [0 for _ in range(len(nums))]

        l = 0
        r = len(nums)-1

        while l<=r:
            t1 = nums[l]
            t2 = nums[r]
            if sum_int[t1-1] >= 1:
                return t1
            sum_int[t1-1]+=1
            
            if sum_int[t2-1] >= 1:
                return t2
            sum_int[t2-1]+=1
            l+=1
            r-=1
        return None


        