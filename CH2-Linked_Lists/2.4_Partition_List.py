# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None :
            return None 
        less = None
        greater = None
        lessStart = None
        greaterStart = None 
        
        while head is not None :
            if head.val < x :
                if less == None :
                    lessStart = head 
                    less = head
                else :
                    less.next = head
                    less = less.next 
            else :
                if greater == None :
                    greaterStart = head
                    greater = head
                else :
                    greater.next = head
                    greater = greater.next 
                
            head = head.next
        if greater is not None :
            greater.next = None 
        else :
            return lessStart 
        
        if less is not None :
            less.next = greaterStart
        else :
            return greaterStart
        
        return lessStart 
