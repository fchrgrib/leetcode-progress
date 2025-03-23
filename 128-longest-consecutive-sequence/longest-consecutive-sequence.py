class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = False
        
        sum_el = 0
        sum_max = -2**31

        for k in h.keys():
            if h[k]:
                continue
            h[k] = True
            
            i=1
            while k-i in h:
                h[k-i] = True
                sum_el+=1
                i+=1
            i=1
            while k+i in h:
                h[k+i] = True
                sum_el+=1
                i+=1
            print(sum_el)
            sum_el+=1
            sum_max = max(sum_el, sum_max)
            sum_el = 0
        if sum_max == -2**31:
            return 0
        return sum_max
        