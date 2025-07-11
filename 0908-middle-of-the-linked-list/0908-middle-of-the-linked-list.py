# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Easiest way to to this is just go through it once to get the length then go to the len // 2
        length = 1
        dummy = head
        while dummy.next is not None:
            length += 1
            dummy = dummy.next
    
        for idx in range(length // 2):
            head = head.next

        return head
            