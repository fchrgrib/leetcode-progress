# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        vst = {}
        tmp = head

        while tmp:
            if tmp.val in vst:
                vst[tmp.val]+=1
            else:
                vst[tmp.val] = 1
            tmp = tmp.next
        tmp_dmy = dummy
        while head:
            while head and vst[head.val]>1:
                head = head.next
            if not head:
                tmp_dmy.next = None
                continue
            tmp_dmy.next = head
            tmp_dmy = tmp_dmy.next
            head = head.next
        return dummy.next
        