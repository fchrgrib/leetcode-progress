class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        nums.sort()
        
        if n == 0:
            return res
        if n == 1:
            res.append([nums[0]])
            return res
        

        def comb(i, arr):
            nonlocal nums, res, n
            if i>=n:
                return
            
            arr.append(nums[i])
            # print(arr)
            res.append(arr[:])

            if i>=n-1:
                return

            for k in range(i, n):
                if i==k:
                    comb(k+1, arr[:])
                    continue

                if arr[-1] == nums[k]:
                    continue
                arr[-1] = nums[k]
                res.append(arr[:])
                comb(k+1, arr[:])
        
        comb(0, [])
        return res