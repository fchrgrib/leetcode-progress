class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        global res
        res = set()
        stack = []

        def bc(l, idx, tiles, stack):
            global res
            if len(l) > len(tiles):
                return
            
            res.add(l)
            temp = l
            for i in range(len(tiles)):
                if i == idx or i in stack:
                    continue
                temp+=tiles[i]
                stack.append(i)
                bc(temp, i, tiles, stack[:])
                stack.pop()
                temp = l
        


        for i in range(len(tiles)):
            stack.append(i)
            bc(tiles[i], i, tiles, stack[:])
            stack.pop()
        
        # print(res)
        return len(res)

            