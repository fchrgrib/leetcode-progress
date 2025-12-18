class Solution:
    def nearestExit(self, m: List[List[str]], e: List[int]) -> int:
        # if e[0] == 0 or e[1] == 0:
        #     return -1
        visited = {}
        step = deque([])
        step.append(([e[0], e[1]], 0))
        visited[(e[0], e[1])] = True

        while len(step) > 0:
            tmp = step.popleft()

            if tmp[0][1]+1<len(m[0]) and (tmp[0][0], tmp[0][1]+1) not in visited and m[tmp[0][0]][tmp[0][1]+1] == ".":
                if tmp[0][1]+1 == len(m[0])-1 or tmp[0][0] == 0 or tmp[0][0] == len(m)-1:
                    return tmp[1]+1
                visited[(tmp[0][0], tmp[0][1]+1)] = True
                step.append(([tmp[0][0], tmp[0][1]+1], tmp[1]+1))
            if tmp[0][1]-1>=0 and (tmp[0][0], tmp[0][1]-1) not in visited and m[tmp[0][0]][tmp[0][1]-1] == ".":
                if tmp[0][1]-1 == 0 or tmp[0][0] == 0 or tmp[0][0] == len(m)-1:
                    return tmp[1]+1
                visited[(tmp[0][0], tmp[0][1]-1)] = True
                step.append(([tmp[0][0], tmp[0][1]-1], tmp[1]+1))
            if tmp[0][0]+1<len(m) and (tmp[0][0] + 1, tmp[0][1]) not in visited and m[tmp[0][0]+1][tmp[0][1]] == ".":
                if tmp[0][0]+1 == len(m)-1 or tmp[0][1] == 0 or tmp[0][1] == len(m[0])-1:
                    return tmp[1]+1
                visited[(tmp[0][0]+1, tmp[0][1])] = True
                step.append(([tmp[0][0]+1, tmp[0][1]], tmp[1]+1))
            if tmp[0][0]-1>=0 and (tmp[0][0] -1, tmp[0][1]) not in visited and m[tmp[0][0]-1][tmp[0][1]] == ".":
                if tmp[0][0]-1 == 0 or tmp[0][1] == 0 or tmp[0][1] == len(m[0])-1:
                    return tmp[1]+1
                visited[(tmp[0][0]-1, tmp[0][1])] = True
                step.append(([tmp[0][0]-1, tmp[0][1]], tmp[1]+1))
        return -1


        