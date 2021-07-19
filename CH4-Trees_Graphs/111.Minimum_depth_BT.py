class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDepth = float('inf')
        if root is None :
            return 0
        return self.traverse(root,1,minDepth) 
        
    def traverse(self,root,currentDepth, minDepth) :
        if root is None :
            return 
        if root.left is None and root.right is None : # leaf node
            minDepth = min(minDepth,currentDepth)
        
        if root.left :
            minDepth = min(minDepth,self.traverse(root.left,currentDepth+1,minDepth))
        if root.right :
            minDepth = min(minDepth,self.traverse(root.right,currentDepth+1,minDepth))
        
        return minDepth
