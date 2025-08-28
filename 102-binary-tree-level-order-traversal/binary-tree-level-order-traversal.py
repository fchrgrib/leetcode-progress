# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        global dp
        dp = {}

        def dfs(root, lvl):
            if not root:
                return
            global dp
            if lvl not in dp:
                dp[lvl] = [root.val]
            else:
                dp[lvl].append(root.val)
            
            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)
        
        dfs(root, 0)
        res = [i for _, i in dp.items()]
        return res