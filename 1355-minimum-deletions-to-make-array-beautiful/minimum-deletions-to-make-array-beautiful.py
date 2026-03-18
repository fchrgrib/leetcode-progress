class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        idx = -1
        lst = 0

        for num in nums:
            if idx%2 == 0 and lst == num:
                continue
            idx+=1
            lst = num
        ln = idx+1 if (idx+1)%2==0 else idx
        return len(nums)-ln
        