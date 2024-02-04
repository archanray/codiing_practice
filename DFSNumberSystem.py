class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def DFS(self, root, path):
        if root is None:
            return path
        else:
            path = path+str(root.val)
        path = self.DFS(root.left, path)
        path = self.DFS(root.right, path)
        return path
    
    def sumNumbers(self, root):
        path = self.DFS(root, "")
        return path

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

q = Solution()
print("checking DFS:", q.sumNumbers(root))