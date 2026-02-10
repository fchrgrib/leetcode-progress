class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        H = list(hamsters)
        bucket = 0

        for i in range(len(H)):
            if H[i] == "H" and i-1>= 0 and H[i-1] == "B":
                continue
            

            if H[i] == "H" and i+1<len(H) and H[i+1] == ".":
                bucket+=1
                H[i+1] = "B"
            elif H[i] == "H" and i-1>=0 and H[i-1] == ".":
                H[i-1] = "B"
                bucket+=1
            elif H[i] == "H":
                return -1
        return bucket

                    



        