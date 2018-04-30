from collections import deque
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

    def isSymmetricIterative(self,root):
        if not root:
            return True
        q = deque()
        q.extend([root, '#'])
        temp = []
        while True:
            if len(q) ==1:
                l = len(temp)//2
                if temp[:l] != list(reversed(temp[l:])):
                    return False
                break
            node = q.popleft()
            if node == '#':
                q.append('#')
                l = len(temp)//2
                if temp[:l] != list(reversed(temp[l:])) and l>0:
                    print(temp)
                    return False
                temp = []
            else:
                if node != None:
                    temp.append(node.val)
                q.extend([node.left,node.right])
        return True

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
print(s.isSymmetricIterative(t))