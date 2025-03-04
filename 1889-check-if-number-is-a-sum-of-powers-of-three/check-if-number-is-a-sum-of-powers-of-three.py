class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def get_the_nearest(n):
            sum = 0
            i = 1
            while(i<n):
                i*=3
                sum+=1

            return sum
        
        def is_true(pow, n):
            if n == 0 :
                return True
            if n<0:
                return False
            
            temp = False

            for i in range(pow,-1,-1):
                temp|=is_true(i-1,n-3**i)
            return temp

        return is_true(get_the_nearest(n), n)