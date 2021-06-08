# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代法

        T: O(N)
        S: O(1)
        """

        if not head or not head.next:
            return head # 易错

        dummy = cur = ListNode(-1)
        dummy.next = head # 易错，需要连接起来

        while cur.next and cur.next.next:
            one = cur.next
            two = cur.next.next
            tree = cur.next.next.next

            cur.next = two
            two.next = one
            one.next = tree

            cur = one

        return dummy.next