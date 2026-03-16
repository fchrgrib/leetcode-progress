class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_stack = deque()
        min_stack = deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            while max_stack and max_stack[-1]<nums[r]:
                max_stack.pop()
            max_stack.append(nums[r])
            while min_stack and min_stack[-1]>nums[r]:
                min_stack.pop()
            min_stack.append(nums[r])

            cost = (max_stack[0] - min_stack[0]) * (r-l+1)
            while cost>k:
                if max_stack[0] == nums[l]:
                    max_stack.popleft()
                if min_stack[0] == nums[l]:
                    min_stack.popleft()
                l+=1
                cost = (max_stack[0] - min_stack[0]) * (r-l+1)
            res+=(r-l+1)
        return res        