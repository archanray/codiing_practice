# given a binary tree, each node has a value which represents 'water flow', separate the tree into 2 trees from the root, so that the difference between sum of water flows of each tree is minimal. this input is was 2 equal length arrays, first one described tree structure where arr[i] was the parent of this node, second one had each nodes value

# store sum of subtree in val
# then check the difference of any node to its sub node
# find the min and return

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorder(self, root):
        if root == None:
            return 0
        root.val += self.postorder(root.left) + self.postorder(root.right)
        return root.val
    
    def preorder(self, root):
        if root == None:
            return 
        
        leftDiff = abs(root.left.val - (root.val-root.left.val))
        rightDiff = abs(root.right.val - (root.val-root.right.val))
        
        self.minDiff = min(self.minDiff, min(leftDiff, rightDiff))
        return
    
    def minAbsDiff(self, root):
        import sys
        self.minDiff = sys.maxsize
        self.postorder(root)
        self.preorder(root)
        return self.minDiff

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

q = Solution()
print(q.minAbsDiff(root))