class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        sum_a = Counter(s1)
        tmp = sum_a.copy()
        set_val = set(list(s1))

        if l2<l1:
            return False
        
        l= 0
        r = 0

        while r<l2:
            if s2[r] in tmp:
                tmp[s2[r]]-=1
                if tmp[s2[r]] == 0:
                    del tmp[s2[r]]
                if not tmp:
                    return True
            else:
                if s2[r] in set_val:
                    while l<r and s2[l] != s2[r]:
                        if s2[l] in set_val:
                            if s2[l] in tmp:
                                tmp[s2[l]]+=1
                            else:
                                tmp[s2[l]]=1
                        l+=1
                    l+=1
                    r+=1
                    continue
                tmp = sum_a.copy()
                l=r
            r+=1

        return False
        

        