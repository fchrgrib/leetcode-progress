class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        gp = {}
        visited = {}
        if source == target:
            return 0

        for i in range(len(routes)):
            for j in routes[i]:
                if j not in gp:
                    gp[j] = [i]
                else:
                    gp[j].append(i)
        if source not in gp or target not in gp:
            return -1
        que = deque([[i,1] for i in gp[source]])

        while len(que)>0:
            tmp = que.popleft()
            if tmp[0] in visited:
                continue
            visited[tmp[0]] = True

            for i in routes[tmp[0]]:
                if i == target:
                    return tmp[1]
                if i in gp:
                    que.extend([[j, tmp[1]+1] for j in gp[i]])
                    gp[i].clear()
        return -1
        