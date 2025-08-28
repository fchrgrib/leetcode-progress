# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, max_el, min_el):
            if not root:
                return True
            if root.val <= min_el or root.val >= max_el:
                return False
            
            return dfs(root.left, root.val, min_el) and dfs(root.right, max_el, root.val)
        if not root or (not root.right and not root.left):
            return True

        return dfs(root, float("inf"), float("-inf"))

        