class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n =  len(grades)
        t = 0
        sum = 0

        while n-t-1>t+1:
            n-=(t+1)
            t+=1
            sum+=1
        return sum+1