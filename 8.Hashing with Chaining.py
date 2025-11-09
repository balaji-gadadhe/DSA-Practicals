# Hash Table Implementation using Separate Chaining
# Supports: Insert, Search, Delete, Display

# Node class to store key-value pairs
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to next node in case of collision

# Fixed hash table size
SIZE = 10
table = [None] * SIZE  # Initialize table with None

# ---------------- HASH FUNCTION ----------------
def hash_func(key):
    # Division method: returns index based on key % SIZE
    return key % SIZE

# ---------------- INSERT ----------------
def insert(key, value):
    i = hash_func(key)
    new_node = Node(key, value)
    
    # If no element exists at index, insert directly
    if not table[i]:
        table[i] = new_node
    else:
        # Collision → use chaining (linked list)
        temp = table[i]
        while temp.next:
            temp = temp.next
        temp.next = new_node
    print("Inserted successfully!")

# ---------------- SEARCH ----------------
def search(key):
    i = hash_func(key)
    temp = table[i]
    # Traverse linked list at this index
    while temp:
        if temp.key == key:
            print("Found! Value:", temp.value)
            return
        temp = temp.next
    print("Key not found!")

# ---------------- DELETE ----------------
def delete(key):
    i = hash_func(key)
    temp = table[i]
    prev = None  
    while temp:
        if temp.key == key:
            # If deleting first node
            if not prev:
                table[i] = temp.next
            else:
                prev.next = temp.next
            print("Deleted successfully!")
            return
        prev=temp
        temp=temp.next
    print("Key not found!")

# ---------------- DISPLAY ----------------
def display():
    print("\n--- Hash Table ---")
    for i in range(SIZE):
        temp = table[i]
        print(f"At index {i}: ", end="")
        while temp:
            print(f"({temp.key}, {temp.value}) -> ", end="")
            temp = temp.next
        print("None")

# ---------------- MENU ----------------
def Menu():
    while True:
        print("\n--- Hash Table Operations ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key (integer): "))
            value = input("Enter value: ")
            insert(key, value)

        elif choice == 2:
            key = int(input("Enter key to search: "))
            search(key)

        elif choice == 3:
            key = int(input("Enter key to delete: "))
            delete(key)

        elif choice == 4:
            display()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the menu
Menu()
