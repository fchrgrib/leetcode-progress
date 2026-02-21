class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        l_hs, l_ht = len(houses), len(heaters)
        hs = {}
        j = 0


        for i in range(l_hs):
            while j+1<l_ht and abs(heaters[j+1] - houses[i]) <= abs(heaters[j] - houses[i]):
                hs[houses[i]] =  min(hs.get(houses[i], float("inf")), abs(heaters[j+1] - houses[i]))
                j+=1
            hs[houses[i]] =  min(hs.get(houses[i], float("inf")), abs(heaters[j] - houses[i]))
        return max(hs.values())
        