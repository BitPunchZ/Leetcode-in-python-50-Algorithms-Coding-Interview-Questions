class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        turtle = head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if(turtle == hare):
                return True
        return False
