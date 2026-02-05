class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = res = 0
        c_sum = {0:1}

        for i, v in enumerate(nums):
            prefix_sum += v
            
            md = prefix_sum%k

            if md in c_sum:
                res+=c_sum[md]
            
            if md not in c_sum:
                c_sum[md] = 1
            else:
                c_sum[md] += 1
        return res


        