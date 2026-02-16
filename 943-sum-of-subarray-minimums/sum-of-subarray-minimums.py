class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ln = len(arr)
        MOD = 10**9 + 7

        if ln == 1:
            return arr[0]
        
        stack = []
        left = [1] * ln
        right = [1] * ln

        for i in range(ln-1, -1, -1):
            while stack and arr[stack[-1]]>arr[i]:
                idx = stack.pop()
                left[idx] = idx - i
            stack.append(i)
        while stack:
            idx = stack.pop()
            left[idx] = idx + 1
        
        for i in range(ln):
            while stack and arr[stack[-1]]>=arr[i]:
                idx = stack.pop()
                right[idx] = i - idx
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            right[idx] = ln - idx
        sm = 0
        for i in range(ln):
            sm+=(left[i]*right[i])*arr[i]
        return sm % MOD
        