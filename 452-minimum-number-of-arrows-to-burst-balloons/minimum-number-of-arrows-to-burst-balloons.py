class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key = lambda x:x[1])
        
        first = points[0]
        res = 1

        for i in range(1, len(points)):
            if first[1]>=points[i][0]:
                continue
            res+=1
            first = points[i]
        return res

        