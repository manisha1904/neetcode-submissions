# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(-1)
        tempList = newList

        while list1 and list2:
            if list1.val <= list2.val:
                tempList.next = list1
                list1 = list1.next
            else:
                tempList.next = list2
                list2 = list2.next
            tempList = tempList.next
        
        if list1:
            tempList.next = list1
        else:
            tempList.next = list2
        
        return newList.next