class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        this is my thought to solve this problem, i will do binary search with the left value is the max of the element of the array nums
        and the right variable will have the sum of nums, i will create some function that called get nums of split array to get the amount of array that
        we can split with the given threshold in the parameter
        """
        l = max(nums)
        r = sum(nums)

        def get_num_split_array(amount):
            nonlocal nums

            split_arr, tmp_sum = 0, 0

            for i in nums:
                tmp_sum+=i
                if tmp_sum == amount:
                    tmp_sum = 0
                    split_arr+=1
                    continue
                if tmp_sum>amount:
                    tmp_sum = i
                    split_arr+=1
                    continue
            if tmp_sum>0:
                split_arr+=1
            return split_arr
        while l<r:
            m = (l+r)//2

            if get_num_split_array(m)<=k:
                r = m
            else:
                l = m+1
        return l