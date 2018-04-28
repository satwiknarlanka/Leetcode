# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isMirror(root.left,root.right)
    
    def isMirror(self,root1,root2):
        if root1 == root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right,root2.left)


#testcase
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
c1 = t.right
c1.left = TreeNode(4)
c1.right = TreeNode(3)
c2 = t.left
c2.left = TreeNode(3)
c2.right = TreeNode(4)
s = Solution()
print(s.isSymmetric(t))