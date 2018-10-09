# Remove kth from end element from the linked ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        curr = head
        while curr is not None:
            size += 1
            curr = curr.next

        target = size - n

        i = 0
        if target == 0:
            return head.next

        curr= head
        while i<target-1:
            curr = curr.next
            i+=1

        curr.next = curr.next.next

        return head


        
