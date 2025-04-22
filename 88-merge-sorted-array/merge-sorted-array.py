class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0 :
            return
        i1 = i2 = c1 = 0
        n1 = m + n
        t1 = nums1[i1]
        t2 = nums2[i2]
        c_n1 = nums1[:m]

        while c1<n1:
            if i1>=len(c_n1):
                while c1<n1:
                    nums1[c1] = nums2[i2]
                    i2+=1
                    c1+=1
                return
            if i2>=n:
                while c1<n1:
                    nums1[c1] = c_n1[i1]
                    i1+=1
                    c1+=1
                return
            if c_n1[i1] < nums2[i2]:
                nums1[c1] = c_n1[i1]
                i1+=1
            else:
                nums1[c1] = nums2[i2]
                i2+=1
            c1+=1
        