class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0
        
        while max_heap or cooldown:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    cooldown.append((time + n, count))
            
            if cooldown and cooldown[0][0] == time:
                available_time, cnt = cooldown.popleft()
                heapq.heappush(max_heap, cnt)
        
        return time
