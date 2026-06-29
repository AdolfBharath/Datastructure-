class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def minimum(self, root):
        while root.left:
            root = root.left
        return root.data

    def maximum(self, root):
        while root.right:
            root = root.right
        return root.data

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# ---------------- MAIN PROGRAM ----------------

tree = BST()

data = [50, 30, 70, 20, 40, 60, 80]

for value in data:
    tree.root = tree.insert(tree.root, value)

print("Inorder:")
tree.inorder(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

print("\n\nSearch 40:", tree.search(tree.root, 40))
print("Search 100:", tree.search(tree.root, 100))

print("Minimum:", tree.minimum(tree.root))
print("Maximum:", tree.maximum(tree.root))

tree.root = tree.delete(tree.root, 50)

print("\nAfter deleting 50:")
tree.inorder(tree.root)
