class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]]<temperatures[i]:
                tmp = i - stack[-1]
                res[stack.pop()] = tmp
            stack.append(i)
        return res
        