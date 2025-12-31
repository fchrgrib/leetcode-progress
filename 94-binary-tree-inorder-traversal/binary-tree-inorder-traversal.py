# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return None
            nonlocal res
            tmp = None
            
            if root.left:
                tmp = dfs(root.left)
            if tmp == None:
                res.append(root.val)
            if root.right:
                tmp = dfs(root.right)
            return None
        
        dfs(root)
        return res
            

        