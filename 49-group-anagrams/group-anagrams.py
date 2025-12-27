class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for i in strs:
            s = list(i)
            s.sort()
            tmp = "".join(s)
            if tmp not in h:
                h[tmp] = [i]
                continue
            h[tmp].append(i)
        
        return [i for _, i in h.items()]


        