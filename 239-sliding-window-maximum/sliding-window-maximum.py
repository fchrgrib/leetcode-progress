class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        res = []
        pq = []

        for i in range(len(nums)):
            while len(pq)>0 and pq[0][1] <= i-k-1:
                heapq.heappop(pq)
            if i >= k:
                tmp = pq[0]
                
                res.append(-tmp[0])
            heapq.heappush(pq, (-nums[i], i))
        
        print(pq)
        while pq[0][1] <= len(nums)-k-1:
            heapq.heappop(pq)
        res.append(-pq[0][0])
            

        return res
        