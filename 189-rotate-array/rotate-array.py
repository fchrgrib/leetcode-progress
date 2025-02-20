class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = [0] * len(nums)
        for i in range(len(nums)):
            c = i-k
            if c<0:
                c = len(nums)+c
            temp[i] = nums[c]

        for i in range(len(nums)):
            nums[i] = temp[i]
        