# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = float("-inf")
        res = 0

        def dfs(root, max_val):
            if root == None:
                return
            
            if root.val >= max_val:
                nonlocal res
                res+=1
                max_val = root.val
            
            if root.left:
                dfs(root.left, max_val)
            if root.right:
                dfs(root.right, max_val)
        dfs(root, max_val)
        return res


        