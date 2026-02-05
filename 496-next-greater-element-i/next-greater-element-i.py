class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        key = {v: i for i, v in enumerate(nums2)}
        l2 = len(nums2)
        res = []

        for i in nums1:
            idx = key[i]
            while idx<l2 and nums2[idx]<=i:
                idx+=1
            if idx != l2:
                res.append(nums2[idx])
            else:
                res.append(-1)
        return res
        