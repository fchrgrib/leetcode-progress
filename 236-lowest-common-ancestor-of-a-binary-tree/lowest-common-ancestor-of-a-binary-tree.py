# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_contain(self, root: 'TreeNode', val:int):
        if not root:
            return False
        
        if root.val == val:
            return True
        lft = self.is_contain(root.left, val)
        if not lft:
            return self.is_contain(root.right, val)
        return lft
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        p_val, q_val, curr_val = p.val, q.val, root.val


        if p_val == curr_val or q_val == curr_val:
            return root

        if not root.right:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if not root.left:
            return self.lowestCommonAncestor(root.right, p, q)

        find_lft, find_right = self.is_contain(root.left, p_val), self.is_contain(root.right, q_val)
        if not find_lft and not find_right:
            find_lft, find_right = self.is_contain(root.left, q_val), self.is_contain(root.right, p_val)

        if find_lft and find_right:
            return root
        elif find_lft:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

        