# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        temp_res.next = head
        left = head
        right = head
        
        for _ in range(n):
            right = right.next
            
        if not right:
            
            return dummy_head.next.next
        
        while right.next:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        
        return dummy_head.next