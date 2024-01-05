class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        pass

class Solution:
    def buildTree(self, preorder, inorder):
        # expected all are unique elements
        if not preorder or not inorder:
            return None
        map_inorder = {val:idx for val,idx in enumerate(inorder)}
        
    
q = Node()
print(q.val)