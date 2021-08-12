# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1 = headA
        node2 = headB
        flag = 0
        dupli = set()

        while node1 is not None :
            dupli.add(node1)
            node1= node1.next

        while node2 is not None :
            if node2 in dupli :
                return node2
            node2 = node2.next

        return None
