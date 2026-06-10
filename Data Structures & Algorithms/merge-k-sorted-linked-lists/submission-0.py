# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        newList = ListNode(-1)
        currList = newList
        while list1 or list2:
            val1 = list1.val if list1 else 10001
            val2 = list2.val if list2 else 10001

            if val1 < val2:
                currList.next = list1
                list1 = list1.next
            else:
                currList.next = list2
                list2 = list2.next
            currList = currList.next

        return newList.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        newList = self.merge(lists[0], lists[1])
        i = 2

        while i < length:
            newList = self.merge(newList, lists[i])
            i += 1
        return newList
