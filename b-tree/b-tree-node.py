class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def display(self, indent="", is_last=True):
        connector = "└── " if is_last else "├── "
        tipo = "Leaf" if self.leaf else "Node"
        print(indent + connector + f"{self.keys} ({tipo})")

        indent += "    " if is_last else "│   "

        if not self.leaf:
            for i, child in enumerate(self.children):
                is_last_child = (i == len(self.children) - 1)
                child.display(indent, is_last_child)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, k, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            return True

        if x.leaf:
            return False

        return self.search(k, x.children[i])

    def display(self):
        self.root.display()

    def insert(self, k):
        if self.search(k):
            return

        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(leaf=False)
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1

        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1

            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)

        x.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]

        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t]

        x.children.insert(i + 1, z)


def main():
    B = BTree(3)

    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in keys:
        B.insert(key)

    print("B-tree structure:")
    B.display()


if __name__ == '__main__':
    main()