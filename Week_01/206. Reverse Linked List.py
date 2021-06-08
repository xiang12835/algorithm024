class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt

        return pre