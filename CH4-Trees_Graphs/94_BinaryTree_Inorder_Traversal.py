# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []
      
        self.traverse(root,values)
        return values
    def traverse(self,root,values) :
        if root is None:
            return
        else :
            self.traverse(root.left,values)
            values.append(root.val)
            self.traverse(root.right,values)
            
