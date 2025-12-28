class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        visited = set()
        max_seq = float("-inf")
        nums = set(nums)
        
        for i in nums:
            if i in visited:
                continue
            curr_seq = 1
            tmp_i = i
            visited.add(i)
            while (tmp_i+1) in nums:
                tmp_i+=1
                curr_seq+=1
                visited.add(tmp_i)
            tmp_i = i
            while (tmp_i-1) in nums:
                tmp_i-=1
                curr_seq+=1
                visited.add(tmp_i)
            max_seq = max(max_seq, curr_seq)
        return max_seq
        