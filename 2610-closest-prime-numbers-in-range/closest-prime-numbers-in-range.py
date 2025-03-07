class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sum = []
        

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        while left<=right:
            if is_prime(left):
                sum.append(left)
            left+=1

        if len(sum)<2:
            return [-1,-1]
        m = sum[1] - sum[0]
        res = [sum[0], sum[1]]
        for i in range(1, len(sum)):
            if m>sum[i] - sum[i-1]:
                res = [sum[i-1], sum[i]]
                m = sum[i] - sum[i-1]
        return res