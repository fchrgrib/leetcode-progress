class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sl = SortedList()
        
        for v in nums:
            index = sl.bisect_right(2 * v)
            
            res += len(sl) - index
            
            sl.add(v)
            
        return res

        