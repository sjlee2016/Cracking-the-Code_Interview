class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        total = 0
        return self.BST(root,low,high,total)
        
    
    def BST(self,root,low,high,total):
        
        if root : 
            if low <= root.val <= high :
                total = total + root.val
            if low < root.val : # don't need to search left child if root val is rleady smaller
                total = self.BST(root.left,low,high,total)
            if high > root.val : # don't need to search right child if root val is already bigger
                total = self.BST(root.right,low,high,total)
                
                
        return total
