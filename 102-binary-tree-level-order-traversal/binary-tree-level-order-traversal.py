# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, r: Optional[TreeNode]) -> List[List[int]]:
        if r == None:
            return []
        
        res = []
        d = {}
        q = deque()
        q.append((r, 0))

        while q:
            t, i = q.popleft()
            if i not in d:
                d[i] = [t.val]
            else:
                d[i].append(t.val)
            if t.left != None:
                q.append((t.left, i +1))
            if t.right != None:
                q.append((t.right, i+1))
        i = 0
        while i in d:
            res.append(d[i])
            i+=1
        return res
        