class Solution:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)

        if ln == 1:
            return 0

        list_jump = deque()
        curr_jump = (nums[0], 1)

        for i in range(1, ln):
            if curr_jump[0]<i+nums[i]:
                list_jump.append((i+nums[i], curr_jump[1]+1))
            if curr_jump[0] >= ln-1:
                return curr_jump[1]
            
            while list_jump and curr_jump[0] == i:
                curr_jump = max(curr_jump, list_jump.popleft())
        return curr_jump[1]
        