class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        j = 0
        res = 0
        
        for house in houses:
            while j + 1 < len(heaters) and abs(heaters[j+1] - house) <= abs(heaters[j] - house):
                j += 1
            
            res = max(res, abs(heaters[j] - house))
        
        return res
        