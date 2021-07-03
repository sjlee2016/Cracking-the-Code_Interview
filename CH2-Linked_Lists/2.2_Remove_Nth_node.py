# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        i = 0
        if head.next is None : 
            return None
        while node is not None : 
            node = node.next 
            i += 1
        node = head 
        
        
        for k in range(0,i-n+1) :
            if k == i-n : 
                if node.next is None :
                    previous.next = None
                else : 
                    node.val = node.next.val
                    node.next = node.next.next 
                break
            previous = node
            node = node.next
            
        return head 
