# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if l == r:
            return head
        tmp_l = l
        tail =  head
        r-=l

        while tail and l>1:
            tail = tail.next
            l-=1
        

        rev = tail
        tmp = rev

        while tmp and r>0:
            tmp = tmp.next
            r-=1
        tail = tmp.next
        tmp.next = None
        
        prev = tail

        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt
        if tmp_l == 1:
            return prev
        tmp =  head
        while tmp_l>2:
            tmp = tmp.next
            tmp_l-=1
        tmp.next = prev
        return head
        