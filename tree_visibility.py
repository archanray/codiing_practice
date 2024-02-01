class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.is_obstructed = False

# basic idea is to do a BFS and then print traverse accordingly
def visible_nodes(root, position):
    if not root:
        return []

    stack = [(root, position)]  # Store nodes and their positions
    visible_nodes = []

    while stack:
        node, direction = stack.pop()

        if direction == "left":
            # Add right child first for left view
            if node.right:
                stack.append((node.right, "right"))
            if node.left:
                stack.append((node.left, direction))
        elif direction == "right":
            # Add left child first for right view
            if node.left:
                stack.append((node.left, "left"))
            if node.right:
                stack.append((node.right, direction))
        else:
            raise ValueError("Invalid position. Must be 'left' or 'right'.")

        visible_nodes.append(node.val)

    return visible_nodes

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

visible_from_left = visible_nodes(root, "left")
visible_from_right = visible_nodes(root, "right")

print("Visible from left:", visible_from_left)
print("Visible from right:", visible_from_right)