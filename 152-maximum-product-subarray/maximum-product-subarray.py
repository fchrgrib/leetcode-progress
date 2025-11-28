class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            current_num = nums[i]
            
            temp_max = max_ending_here
            
            max_ending_here = max(current_num, 
                                  current_num * temp_max, 
                                  current_num * min_ending_here)
            
            min_ending_here = min(current_num, 
                                  current_num * temp_max, 
                                  current_num * min_ending_here)
            
            max_so_far = max(max_so_far, max_ending_here)
            
        return max_so_far
