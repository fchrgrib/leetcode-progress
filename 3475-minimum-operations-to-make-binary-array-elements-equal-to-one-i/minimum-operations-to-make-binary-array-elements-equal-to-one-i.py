class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_reverse(n):
            if n == 1:
                return 0
            else:
                return 1
        ln = len(nums)
        swap = 0
        
        for i in range(ln):
            if nums[i] == 1:
                continue
            if i+2>=ln:
                return -1
            nums[i] = get_reverse(nums[i])
            nums[i+1] = get_reverse(nums[i+1])
            nums[i+2] = get_reverse(nums[i+2])
            swap+=1
        return swap
                
        