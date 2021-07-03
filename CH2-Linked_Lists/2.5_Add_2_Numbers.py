# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        result = None
        flag = 0
        while l1 is not None and l2 is not None : 
            node = ListNode()
            node.next = None 
            s = l1.val + l2.val + flag 
            if s >= 10 :
                flag = 1 
                node.val = s-10 
            else :
                node.val = s
                flag = 0 
                
            if result == None :
                head = node
                result = node
            else :
                result.next = node
                result = result.next     
            l1 = l1.next
            l2 = l2.next 
            
        while l1 is not None :
            node = ListNode()
            node.next = None 
            s = l1.val + flag 
            if s >= 10 :
                flag = 1 
                node.val = s-10 
            else :
                node.val = s
                flag = 0 
            result.next = node
            result = result.next
            l1 = l1.next 
            
        while l2 is not None :
            node = ListNode()
            node.next = None 
            s = l2.val + flag 
            if s >= 10 :
                flag = 1 
                node.val = s-10 
            else :
      
