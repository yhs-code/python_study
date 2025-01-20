class Node:
    def __init__(self, elem=1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []

    def level_build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                self.help_queue.pop(0)

    def pre_order(self, node: Node):
        if node:
            print(node.elem, end=" ")
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)

    def in_roder(self, node: Node):
        if node:
            self.in_roder(node.lchild)
            print(node.elem, end=" ")
            self.in_roder(node.rchild)

    def post_order(self, node: Node):
        if node:
            self.post_order(node.lchild)
            self.post_order(node.rchild)
            print(node.elem, end=" ")

    def level_order(self):
        help_queue = []
        help_queue.append(self.root)
        while help_queue:
            current_node: Node = help_queue.pop(0)
            print(current_node.elem, end=" ")
            if current_node.lchild is not None:
                help_queue.append(current_node.lchild)
            if current_node.rchild is not None:
                help_queue.append(current_node.rchild)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.level_build_tree(new_node)
    tree.pre_order(tree.root)
    print()
    tree.in_roder(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.level_order()
