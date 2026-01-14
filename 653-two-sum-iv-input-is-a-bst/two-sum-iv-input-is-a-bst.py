# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()

        def dfs(root):
            if not root:
                return
            
            visited.add(root.val)
            dfs(root.left)
            dfs(root.right)
        def find_sub(root):
            nonlocal k
            if not root:
                return False
            tmp = k-root.val
            if tmp in visited and tmp != 0 and tmp !=root.val:
                return True
            return find_sub(root.right) or find_sub(root.left)
        dfs(root)
        return find_sub(root)

        