class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # My thought for this problem is using counter for each s1 and s2 and compare each other
        # if the counter is same, for example {a:2, b:2} in each s1 and s2 it will return True and if its not, it will return zero
        c_s1 = Counter(s1)
        l_s1 = len(s1)
        c_s2 = {}

        for index, i in enumerate(s2):
            if i in c_s2:
                c_s2[i] += 1
            else:
                c_s2[i] = 1
            
            if index>l_s1-1:
                store = s2[index-l_s1]
                c_s2[store]-=1
                if c_s2[store]<=0:
                    del c_s2[store]
            
            if c_s2 == c_s1:
                return True

        return False


        