# Given the root of a binary tree, return the maximum path sum of any non-empty path.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            max_sum = max(max_sum, left + right + node.val)
            return max(left, right) + node.val
        max_sum = float('-inf')
        dfs(root)
        return max_sum

input = TreeNode(1, TreeNode(2), TreeNode(3))
q = Solution()
print(q.maxPathSum(input)) #Output: 6