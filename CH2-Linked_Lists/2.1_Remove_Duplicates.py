class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None :
            return None 
        previous = head
        node = head.next 
        
        while node is not None :
            if node.val == previous.val : 
                previous.next = node.next
            else :
                previous = node 
            node = node.next 
        
            
        return head 
