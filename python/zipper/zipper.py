class Zipper:
    def __init__(self, tree, focus=None, parent=None):
        self.root = tree
        self.focus = focus if focus else tree
        self.parent = parent if parent else None

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.focus["value"]

    def set_value(self, value):
        self.focus["value"] = value
        return self

    def left(self):
        return (
            Zipper(self.root, self.focus["left"], self) if self.focus["left"] else None
        )

    def set_left(self, node):
        self.focus["left"] = node
        return self

    def right(self):
        return (
            Zipper(self.root, self.focus["right"], self)
            if self.focus["right"]
            else None
        )

    def set_right(self, node):
        self.focus["right"] = node
        return self

    def up(self):
        return self.parent

    def to_tree(self):
        return self.root
