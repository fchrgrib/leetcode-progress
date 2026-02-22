class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque()
        ln = len(nums)
        dp = [0]*ln

        for i in range(ln):
            if queue:
                dp[i] = nums[i] + dp[queue[0]]
            else:
                dp[i] = nums[i]
            
            while queue and dp[queue[-1]]<=dp[i]:
                queue.pop()
            while queue and queue[0]<=i-k:
                queue.popleft()
            queue.append(i)
        print(dp)
        return dp[ln-1]

        