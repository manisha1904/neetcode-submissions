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
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next