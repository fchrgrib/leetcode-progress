class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k == 0:
            ct = Counter(nums)

            for _, val in ct.items():
                if val>1:
                    res+=1
            return res
        
        ln = len(nums)

        if ln == 1:
            return 0

        nums.sort()
        l, r = 0, 1

        while r<ln:
            while (r<ln and abs(nums[r] - nums[l])<k) or (r+1<ln and nums[r] == nums[r+1]):
                r+=1
            while r<ln and l<r and abs(nums[r] - nums[l])>k:
                l+=1
            if r<ln and abs(nums[r]-nums[l]) == k:
                res+=1
            
            r+=1
        return res
        