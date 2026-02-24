class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_el, partition = float("-inf"), 0

        for i in range(len(arr)):
            max_el = max(max_el, arr[i])
            if max_el == i:
                partition+=1

        return partition
        