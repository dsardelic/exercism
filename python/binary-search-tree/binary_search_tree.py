class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data):
        self._root = None
        for data in tree_data:
            self.add(data)

    def data(self):
        return self._root

    def sorted_data(self):
        def inorder(node):
            return sum(
                (
                    inorder(node.left) if node.left else [],
                    [node.data],
                    inorder(node.right) if node.right else [],
                ),
                start=[],
            )

        if not self._root:
            return []
        return inorder(self._root)

    def add(self, data):
        def add_to_node(node):
            if data <= node.data:
                if node.left:
                    add_to_node(node.left)
                else:
                    node.left = TreeNode(data)
            elif node.right:
                add_to_node(node.right)
            else:
                node.right = TreeNode(data)

        if not self._root:
            self._root = TreeNode(data)
        else:
            add_to_node(self._root)
