class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        queue = deque()
        queue.append(("0000", 0))
        
        while queue:
            key, count = queue.popleft()

            for i in range(4):
                num = int(key[i])
                prev = num-1 if num>0 else 9
                next = (num+1)%10

                prev_key = key[:i]+str(prev)+key[i+1:]
                next_key = key[:i]+str(next)+key[i+1:]
                if prev_key == target or next_key == target:
                    return count + 1
                if prev_key not in deadends:
                    queue.append((prev_key, count+1))
                    deadends.add(prev_key)
                if next_key not in deadends:
                    queue.append((next_key, count+1))
                    deadends.add(next_key)


        return -1
        