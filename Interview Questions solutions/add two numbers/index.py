# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer = ans

        carry = 0
        sum = 0

        while(l1!=None or l2!=None):
            sum = carry
            if(l1!=None):
                sum+=l1.val
                l1 = l1.next
            if(l2!=None):
                sum+=l2.val
                l2 = l2.val
            
            carry = int(sum/10)
            pointer.next  = ListNode(sum%10)

            pointer = pointer.next
        
        if(carry>0):
            pointer.next = ListNode(carry)
        
        return ans.next