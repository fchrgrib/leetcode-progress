class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln == 1:
            return [-1]
        res = [-1 for _ in range(ln)]
        stack = []
        
        for i in range(2*ln-1):
            while stack and nums[stack[-1]]<nums[i%ln]:
                tmp = stack.pop()
                res[tmp] = nums[i%ln]
            if i<ln:
                stack.append(i)
        

        return res
