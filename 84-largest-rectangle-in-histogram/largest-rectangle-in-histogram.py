class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ln = len(heights)

        if ln == 1:
            return heights[0]

        width = [1] * ln
        res = 0
        stack = []

        for i in range(ln):
            while stack and heights[stack[-1]]>heights[i]:
                start = stack.pop()
                width[start] += (i-start-1)
            stack.append(i)

        while stack:
            start = stack.pop()
            width[start] += (ln-start-1)

        for i in range(ln-1, -1, -1):
            while stack and heights[stack[-1]]>heights[i]:
                start = stack.pop()
                width[start] += (start-i-1)
            stack.append(i)

        while stack:
            start = stack.pop()
            width[start] += (start)

        for i in range(ln):
            res = max(res, heights[i]*width[i])
        return res
        