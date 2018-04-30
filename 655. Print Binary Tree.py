from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [[]]
        m = self.treeheight(root)
        n = 2 ** m - 1
        result = []
        q = deque()
        q.append(root)
        q.append('#')
        temp = []
        blocksize = n
        while blocksize>0:
            node = q.popleft()
            if node == '#':
                q.append('#')
                ans = []
                for x in temp:
                    block = [''] * blocksize
                    block[(blocksize-1)//2] = str(x)
                    ans.extend(block)
                    ans.append('')
                ans.pop()
                blocksize = (blocksize-1)//2
                result.append(ans)
                temp = []
            else:
                if(node.left != None):
                    q.append(node.left)
                else:
                    q.append(TreeNode(''))
                if(node.right != None):
                    q.append(node.right)
                else:
                    q.append(TreeNode(''))
                temp.append(node.val)
        return result


    def treeheight(self,root):
        if not root:
            return 0
        return max(self.treeheight(root.left),self.treeheight(root.right))+1

#test case
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
print(s.printTree(t))