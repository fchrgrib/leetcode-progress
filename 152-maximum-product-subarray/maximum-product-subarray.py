class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def product_all(arr, s, e):
            sum = 1
            for i in range(s, e+1):
                sum*=arr[i]
            return sum
        def find_first(arr, a,e):
            for i in  range(a,e+1):
                if arr[i]>0:
                    return i
            return -1
        
        neg_arr = []
        max_product = -2**31
        curr_product = 1
        a_noll=0

        for i in range(len(nums)):
            l = len(neg_arr)

            if nums[i] == 0:
                neg_arr.clear()
                curr_product = 1
                max_product = max(0, max_product)
                a_noll=i+1
                continue
            if nums[i] < 0:
                if l>0:
                    if l%2==0:
                        curr_product = product_all(nums, neg_arr[0]+1, i)
                    else:
                        tmp = find_first(nums,a_noll,neg_arr[0])
                        curr_product = product_all(nums, tmp if tmp!= -1 else neg_arr[0], i)
                    max_product = max(curr_product, max_product)
                else:
                    curr_product *=nums[i]
                    max_product = max(max_product, curr_product)
                    curr_product = 1
                    
                neg_arr.append(i)
                continue
            
            curr_product*=nums[i]
            max_product = max(max_product, max(curr_product, nums[i]))
        
        return max_product
