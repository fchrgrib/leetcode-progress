# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """

        if head == None:
            return []
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next

        res = [[-1 for _ in range(n)] for _ in range(m)]
        def fill_res(start, col, row, idx) :
            if (start >= col or start >= row) and idx>=len(tmp):
                return
            
            for i in range(start, col):
                if idx>=len(tmp):
                        continue
                res[start][i] = tmp[idx]
                idx+=1
            for i in range(start+1, row):
                if idx>=len(tmp):
                        continue
                res[i][col-1] = tmp[idx]
                idx+=1
            
            if start<col-1:
                for i in range(col-2, start-1,-1):
                    if idx>=len(tmp):
                        continue
                    res[row-1][i] = tmp[idx]
                    idx+=1

            if start<row-1:
                for i in range(row-2, start,-1):
                    if idx>=len(tmp):
                        continue
                    res[i][start] = tmp[idx]
                    idx+=1

            # print(res)

            fill_res(start +1, col-1, row-1, idx)
        
        fill_res(0, n, m, 0)
        return res
        
        