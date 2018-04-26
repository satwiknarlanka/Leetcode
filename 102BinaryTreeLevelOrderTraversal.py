from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if(root == None):
        return []
    if(root.left == None and root.right == None):
        return [[root.val]]
    q = deque()
    q.append(root)
    q.append('#')
    result = []
    temp = []
    while(True):
        if(len(q) == 1):
            result.append(temp)
            break
        node = q.popleft()
        if(node == '#'):
            q.append('#')
            result.append(temp)
            temp = []
        else:
            if(node.left != None):
                q.append(node.left)
            if(node.right != None):
                q.append(node.right)
            temp.append(node.val)
    return result


#test case
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
c = t.right
c.left = TreeNode(15)
c.right = TreeNode(7)

result = levelOrder(t)
print(result)