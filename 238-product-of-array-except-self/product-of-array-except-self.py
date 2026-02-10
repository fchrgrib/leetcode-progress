class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        is_all_nol = False
        idx_nol = -1
        product = 1

        for i, val in enumerate(nums):
            if val == 0:
                if idx_nol != -1:
                    is_all_nol = True
                    break
                idx_nol = i
                continue
            product*=val
        
        if is_all_nol:
            return [0] * len(nums)
        res = []
        if idx_nol != -1:
            for i in nums:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        
        for i in nums:
            res.append(product//i)
        return res
            
        