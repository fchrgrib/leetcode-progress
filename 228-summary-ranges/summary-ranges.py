class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stack = []
        res = []

        def res_intv(stack):
            end = stack.pop()
            if stack:
                while stack:
                    start = stack.pop()
                return f"{start}->{end}"
            else:
                return f"{end}"

        for i in nums:
            if stack and not stack[-1] + 1 == i:
                res.append(res_intv(stack))
            stack.append(i)
        if stack:
            res.append(res_intv(stack))
        return res
        