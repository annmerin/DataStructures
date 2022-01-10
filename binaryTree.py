class BinaryTreeSearchNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeSearchNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeSearchNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []

        # visit root node
        elements.append(self.data)

        # visit left node
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right node
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # vist left node
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right node
        if self.right:
            elements += self.right.post_order_traversal()

        # visit root node
        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinaryTreeSearchNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




