# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n+=1
        
        k%=n
        if k == 0 :
            return head
        
        tail.next = head
        tail = tail.next

        while n>k+1:
            tail = tail.next
            n-=1
        new_head = tail.next
        tail.next = None
        
        return new_head
        