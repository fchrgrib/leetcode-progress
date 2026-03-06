class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = defaultdict(int)
        prefix_sum = 0
        res = [0] *n

        for start, end, st in bookings:
            seats[start-1]+=st
            seats[end]-=st
        
        for i in range(n):
            prefix_sum+=seats[i]
            res[i] = prefix_sum
        return res
        