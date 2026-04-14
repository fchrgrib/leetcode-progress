class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = baskets[start]
                return
            mid = (start + end) // 2
            build(2*node, start, mid)
            build(2*node+1, mid+1, end)
            tree[node] = max(tree[2*node], tree[2*node+1])
        
        def update(node, start, end, idx):
            if start == end:
                tree[node] = 0
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2*node, start, mid, idx)
            else:
                update(2*node+1, mid+1, end, idx)
            tree[node] = max(tree[2*node], tree[2*node+1])
        
        def query_leftmost(node, start, end, fruit):
            if tree[node] < fruit:
                return -1
            if start == end:
                return start
            mid = (start + end) // 2
            left_result = query_leftmost(2*node, start, mid, fruit)
            if left_result != -1:
                return left_result
            return query_leftmost(2*node+1, mid+1, end, fruit)
        
        build(1, 0, n-1)
        
        unplaced = 0
        for fruit in fruits:
            idx = query_leftmost(1, 0, n-1, fruit)
            if idx == -1:
                unplaced += 1
            else:
                update(1, 0, n-1, idx)
        
        return unplaced