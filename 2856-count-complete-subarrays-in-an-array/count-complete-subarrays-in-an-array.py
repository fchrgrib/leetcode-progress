class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s_num = len(set(nums))
        n = len(nums)

        l = sum = 0
        r = 1

        while l < n:
            s_tmp = len(set(nums[l:r]))
            if s_tmp == s_num:
                l+=1
                sum+=(n-r + 1)
            elif r == n:
                l+=1
            else:
                r+=1
            
        return sum
        