# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def max_rob(root):
            if root == None:
                return (0, 0)
            l = max_rob(root.left)
            r = max_rob(root.right)

            return (root.val + l[1] + r[1], max(l[0], l[1]) + max(r[0], r[1]))
        return max(max_rob(root))


        