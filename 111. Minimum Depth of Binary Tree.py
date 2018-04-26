from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        q = deque()
        q.append(root)
        q.append('#')
        result = 1
        while(True):
            node = q.popleft()
            if(node == '#'):
                q.append('#')
                result += 1
            else:
                if node.left == None and node.right == None:
                    break
                if(node.left != None):
                    q.append(node.left)
                if(node.right != None):
                    q.append(node.right)
        return result

#test case
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
c = t.right
c.left = TreeNode(15)
c.right = TreeNode(7)
s = Solution()
result = s.minDepth(t)
print(result)