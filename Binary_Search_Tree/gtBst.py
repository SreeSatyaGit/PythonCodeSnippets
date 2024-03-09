class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

sortedArr = []
def bfs(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        if current_node is not None:
            sortedArr.append(current_node.value)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            sortedArr.append("null")

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.right.right = TreeNode(12)


bfs(root)
print(sortedArr)

