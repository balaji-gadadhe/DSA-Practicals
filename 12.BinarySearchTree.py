# Binary Search Tree Implementation
# Operations: Insert, Delete, Display, Search

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None 

    # ---------------- INSERT ----------------
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # ---------------- SEARCH ----------------
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # ---------------- DELETE ----------------
    def delete(self, root, key):
        if root is None:
            return root

        # Search for node to delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node found
            # Case 1: No child / only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 2: Two children
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Helper function for delete
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ---------------- DISPLAY (Traversals) ----------------
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

# ---------------- MENU-DRIVEN PROGRAM ----------------
def main():
    bst = BST()
    root = None

    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert Node")
        print("2. Delete Node")
        print("3. Search Node")
        print("4. Display Tree (Inorder, Preorder, Postorder)")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            root = bst.insert(root, key)
            print(f"{key} inserted successfully!")

        elif choice == 2:
            key = int(input("Enter value to delete: "))
            root = bst.delete(root, key)
            print(f"{key} deleted successfully (if it existed).")

        elif choice == 3:
            key = int(input("Enter value to search: "))
            result = bst.search(root, key)
            if result:
                print(f"{key} found in BST.")
            else:
                print(f"{key} not found in BST.")

        elif choice == 4:
            print("\nInorder Traversal: ", end="")
            bst.inorder(root)
            print("\nPreorder Traversal: ", end="")
            bst.preorder(root)
            print("\nPostorder Traversal: ", end="")
            bst.postorder(root)
            print()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

# Run the program
main()
