class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        temp = nums[:]
        for i in range(len(nums)):
            c = i-k
            if c<0:
                c = len(nums)+c
            nums[i] = temp[c]