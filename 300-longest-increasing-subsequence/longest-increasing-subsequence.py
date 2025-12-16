class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                idx = bisect_left(tails, num)
                tails[idx] = num
                
        return len(tails)
        