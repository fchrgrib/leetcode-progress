class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cp = defaultdict(int)
        prefix_sum = 0

        for num, fr, to in trips:
            cp[fr]+=num
            cp[to]-=num
        for key in sorted(cp.keys()):
            prefix_sum+=cp[key]
            if prefix_sum>capacity:
                return False
        return True
        