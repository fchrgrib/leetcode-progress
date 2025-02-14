class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        arr_sum = sum(matchsticks)
        matchsticks = sorted(matchsticks, reverse=True)

        if arr_sum<4:
            return False
        if arr_sum % 4 != 0:
            return False
        
        global edge
        edge = arr_sum/4

        def bc(sum1, sum2, sum3, sum4, idx):
            global edge
            if sum1 == sum2 == sum3 == sum4 == edge:
                return True
            if idx>=len(matchsticks) or sum1>edge or sum2>edge or sum3>edge or sum4>edge:
                return False
            t = matchsticks[idx]
            return bc(sum1+t, sum2, sum3, sum4, idx+1) or bc(sum1, sum2+t, sum3, sum4, idx+1) or bc(sum1, sum2, sum3+t, sum4, idx+1) or bc(sum1, sum2, sum3, sum4+t, idx+1) 
        
        return bc(0, 0, 0, 0, 0)
        