# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast = head
        cnt = 1
        while fast and cnt < k:
            fast = fast.next
            cnt += 1

        if not fast:
            return head

        nxtHead = fast.next
        fast.next = None
        fast = self.reverse(head)
        head.next = self.reverseKGroup(nxtHead, k)

        return fast


        
