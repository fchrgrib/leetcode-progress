class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        ln = len(nums)
        l = 0
        pos_neg = [0,0]

        def get_long(i):
            if i>=ln:
                return 0
            while pos_neg[0]%2 == 1:
                if nums[i]>0:
                    pos_neg[1]-=1
                else:
                    pos_neg[0]-=1
                i+=1
            return pos_neg[1] + pos_neg[0]

        for r in range(ln):
            if nums[r] == 0:
                res = max(res, get_long(l))
                pos_neg = [0,0]
                l = r+1
                continue
            
            if nums[r]>0:
                pos_neg[1]+=1
            else:
                pos_neg[0]+=1
            
            if pos_neg[0]%2==0:
                res = max(res, pos_neg[0]+pos_neg[1])
        return max(res, get_long(l))
                
                
        