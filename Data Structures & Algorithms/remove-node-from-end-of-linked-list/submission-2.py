# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next
        
         # Walk both until fast falls off the end
        while fast:
            slow = slow.next
            fast = fast.next
        # slow is now just before the target

        slow.next = slow.next.next

        return dummy.next


        