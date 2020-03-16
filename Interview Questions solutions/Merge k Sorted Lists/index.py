# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        cur = ListNode(0)
        ans = cur

        while(l1 and l2):
            if(l1.val > l2.val):
                cur.next = l2
                l2 = l2.next

            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(len(lists) == 0):
            return None

        i = 0
        last = len(lists)-1
        j = last

        while(last != 0):
            i = 0
            j = last

            while(j > i):
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j

        return lists[0]
