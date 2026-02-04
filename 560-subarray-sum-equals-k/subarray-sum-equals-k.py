class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        
        len_obj = 0
        hash = {0:1}
        for i, v in enumerate(nums):
            prefix_sum += v

            if prefix_sum - k in hash:
                len_obj += hash[prefix_sum - k]
            
            if prefix_sum not in hash:
                hash[prefix_sum] = 1
            else:
                hash[prefix_sum] += 1
        
        return len_obj

        