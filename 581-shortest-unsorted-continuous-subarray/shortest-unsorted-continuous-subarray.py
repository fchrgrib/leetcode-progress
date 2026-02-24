class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 0
        
        stack = []
        start, end = float("inf"), float("-inf")

        for idx, val in enumerate(nums):
            while stack and nums[stack[-1]]>val:
                st = stack.pop()
                start = min(start, st)
                end = max(end, idx)
            stack.append(idx)
        if start == float("inf") or end == float("-inf"):
            return 0
        mn = min(nums[start:end+1])
        mx = max(nums[start:end+1])
        while end+1<ln and nums[end+1]<mx:
            end+=1
        while start > 0 and nums[start-1] > mn:
            start -= 1
        return end-start+1
                
        