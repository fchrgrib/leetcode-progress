# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        tmp = ListNode()
        res = tmp

        if list1 != None and list2 != None:
            if list1.val<list2.val :
                tmp.val = list1.val
                list1 = list1.next
            else:
                tmp.val = list2.val
                list2 = list2.next
        elif list1 != None:
            tmp.val = list1.val
            list1 = list1.next
        elif list2 != None:
            tmp.val = list2.val
            list2 = list2.next
        else:
            res = None
        
        if list1 != None or list2 != None:
                tmp.next = ListNode()
                tmp = tmp.next
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val<list2.val :
                    tmp.val = list1.val
                    list1 = list1.next
                else:
                    tmp.val = list2.val
                    list2 = list2.next
            elif list1 != None:
                tmp.val = list1.val
                list1 = list1.next
            else:
                tmp.val = list2.val
                list2 = list2.next
            if list1 != None or list2 != None:
                tmp.next = ListNode()
                tmp = tmp.next
        return res
        