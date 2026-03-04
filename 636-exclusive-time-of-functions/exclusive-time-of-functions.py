class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0


        for task in logs:
            id, typ, curr = task.split(":")
            curr = int(curr)
            id = int(id)
            if "start" == typ:
                if stack:
                    res[stack[-1]]+=(curr-prev)
                stack.append(id)
                prev = curr
            else:
                res[stack[-1]]+=(curr-prev+1)
                stack.pop()
                prev = curr+1

        return res
        