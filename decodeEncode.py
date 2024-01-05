class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        pass

class Solution:
    def buildTree(self, preorder, inorder, IDX):
        # expected all are unique elements
        if not preorder or not inorder:
            return None
        if len(preorder) == len(inorder):
            self.root = self.TreeNode()
        map_inorder = {val:idx for val,idx in enumerate(inorder)}
        rootVal = preorder[IDX]
        inorder_IDX = map_inorder[rootVal]
        self.buildTree(preorder, inorder[:inorder_IDX], IDX+1)

q = Node()
print(q.val)