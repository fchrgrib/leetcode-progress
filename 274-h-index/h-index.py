class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        n = len(citations)
        sum = 0

        for i in range(n-1, -1, -1):
            if n-i<=citations[i]:
                sum+=1
        
        return sum

        