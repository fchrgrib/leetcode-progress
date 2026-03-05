class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        lp = len(popped)
        stack = []

        for i in pushed:
            stack.append(i)
            while stack and pop_idx<lp and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx+=1
        return len(stack) == 0
        