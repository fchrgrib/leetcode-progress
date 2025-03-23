# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = []

        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            val.append(t.val)
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)
        val.sort()
        return val[k-1]
            
        