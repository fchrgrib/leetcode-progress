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
            diff = nums[r] - nums[l]

            if diff < k:
                r += 1

            elif diff > k:
                l += 1

            else:
                res += 1
                l += 1
                while l < ln and nums[l] == nums[l-1]:
                    l += 1
        return res
        