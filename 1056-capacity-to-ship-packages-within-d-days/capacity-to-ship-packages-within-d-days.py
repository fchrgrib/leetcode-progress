class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights) + 1
        res = float("inf")

        def is_valid_days(amount):
            nonlocal weights, days

            count_days = 0
            tmp_amount = 0

            for i in weights:
                tmp_amount+=i
                if tmp_amount == amount:
                    count_days+=1
                    tmp_amount = 0
                    continue
                if tmp_amount > amount:
                    tmp_amount = i
                    count_days+=1
            if tmp_amount>0:
                count_days+=1
            return count_days
        m = 0
        while l<r:
            m = (l+r)//2
            
            tmp = is_valid_days(m)
            if tmp <= days:
                res = min(res, m)

            if tmp > days:
                l = m+1
            else:
                r = m
        return res

        



        