# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        global l, r
        l = []
        r = []

        def dfs(ro, is_left):
            if ro == None:
                return
            
            if is_left:
                global l
                l.append(ro.val)

                if ro.left:
                    dfs(ro.left, is_left)
                else:
                    l.append(None)
                if ro.right:
                    dfs(ro.right, is_left)
                else:
                    l.append(None)
            else:
                global r
                r.append(ro.val)

                if ro.right:
                    dfs(ro.right, is_left)
                else:
                    r.append(None)
                if ro.left:
                    dfs(ro.left, is_left)
                else:
                    r.append(None)
        
        dfs(root, True)
        dfs(root, False)

        return l==r
