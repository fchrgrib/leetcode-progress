class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        atmost_k = 0
        atmost_kk = 0
        l, ll = 0, 0
        ln = len(nums)
        sm, smk = 0, 0


        for i in range(ln):
            if nums[i]%2==1:
                sm+=1
                smk+=1
            
            while l<ln and sm>k:
                if nums[l]%2==1:
                    sm-=1
                l+=1
            while ll<ln and smk>k-1:
                if nums[ll]%2 == 1:
                    smk-=1
                ll+=1
            
            atmost_k+=(i-l+1)
            atmost_kk+=(i-ll+1)
        return atmost_k-atmost_kk

        