class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        front = deque()
        ln = len(nums)

        for i in range(ln):
            step = i
            curr_num = nums[i]
            front.append(nums[i])
            while front and step>0 and i!=0:
                front.append((front.popleft()+curr_num)%10)
                curr_num = front[-1]
                step-=1
        return front[-1]
        