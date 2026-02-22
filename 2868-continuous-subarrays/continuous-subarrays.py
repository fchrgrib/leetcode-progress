class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_queue = deque()
        min_queue = deque()
        left, ln = 0, len(nums)
        res = 0
        for i in range(ln):
            while max_queue and max_queue[-1]<nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])

            while min_queue and min_queue[-1]>nums[i]:
                min_queue.pop()
            min_queue.append(nums[i])

            while min_queue and max_queue and abs(max_queue[0]-min_queue[0])>2:
                tmp = nums[left]

                if tmp == max_queue[0]:
                    max_queue.popleft()
                if tmp == min_queue[0]:
                    min_queue.popleft()
                left+=1
            res+=(i - left + 1)
            
        return res
        