class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # in this problem i want to solve with bfs algorithm
        # the solution will have O(MxN) complexity for time and space
        # first we validate if the top left and the right left will not have number 1, if they have return -1
        # we will create queue variable to store all the nodes that we want to visit
        # we will change the node from 0 to 1 too if they already visited and i think we shouldnt create variable visited due to efficiency
        # we never the queue is empty and we not reach the bottom right, we will return -1

        row, col = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        queue = deque()
        queue.append(((0, 0), 1))
        grid[0][0] = 1

        direct = [(1,0), (0,1), (1, 1), (-1,-1), (1, -1), (-1,1), (0,-1), (-1,0)]


        while queue:
            coor, count = queue.popleft()

            if coor[0] == row-1 and coor[1] == col -1:
                return count
            
            for i in direct:
                dx, dy = coor[0] + i[0], coor[1] + i[1]

                if dx<0 or dx>=row or dy<0 or dy>=col:
                    continue
                if grid[dx][dy] == 1:
                    continue
                if dx == row -1 and dy == col -1:
                    return count + 1
                grid[dx][dy] = 1
                queue.append(((dx, dy), count+1))
        return -1






        