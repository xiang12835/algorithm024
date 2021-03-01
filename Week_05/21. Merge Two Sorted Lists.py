# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        法一：迭代法 + 哨兵
        T: O(m+n)
        S: O(1)
        """
        dummy = tmp = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
            
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        
        return dummy.next