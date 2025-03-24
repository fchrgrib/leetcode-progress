class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        arr = [str(i+1) for i in range(n)]
        res = ""

        def fa(n):
            if n ==1:
                return 1
            return n*fa(n-1)

        while len(arr)>0:
            if k == 0 :
                for i in arr:
                    res+=i
                arr.clear()
                return res
            if len(arr) == 1:
                return res+arr[0]
            s = fa(len(arr)-1)
            tmp = 1
            while s*tmp<k:
                tmp+=1
            
            c = arr[tmp-1]
            res+=c
            arr.remove(c)
            k-=s*(tmp-1)
        return res
        