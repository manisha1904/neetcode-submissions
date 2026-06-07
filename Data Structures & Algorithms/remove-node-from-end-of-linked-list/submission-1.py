# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def findLength(head: ListNode) -> int:
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1

    return length

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = findLength(head)
        nthFromStart = length - n

        if length == 1:
            return None

        if nthFromStart == 0:
            result = head.next
            del(head)
            return result

        temp = head
        for i in range(nthFromStart - 1):
            temp = temp.next

        delNode = temp.next
        temp.next = temp.next.next
        del(delNode)

        return head