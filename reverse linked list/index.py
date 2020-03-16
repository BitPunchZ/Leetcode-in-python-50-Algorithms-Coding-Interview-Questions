# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while(head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        return node
