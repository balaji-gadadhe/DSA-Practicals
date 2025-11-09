# Hash Table Implementation using Linear Probing

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Hash function (Division method)
    def hash_function(self, key):
        return key % self.size

    # Insert key
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index  # to detect full table condition
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == start_index:
                print("❌ Hash Table is full! Cannot insert.")
                return
        self.table[index] = key
        print("✅ Key inserted successfully!")

    # Search key
    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"🔍 Key {key} found at index {index}")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print("❌ Key not found in hash table.")

    # Delete key
    def delete(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                print("🗑️ Key deleted successfully!")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print("❌ Key not found. Cannot delete.")

    # Display hash table
    def display(self):
        print("\n📘 Hash Table State:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


# --- MAIN PROGRAM ---
hash_table = HashTable()

while True:
    print("\n====== HASH TABLE (LINEAR PROBING) ======")
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key (integer): "))
        hash_table.insert(key)

    elif choice == '2':
        key = int(input("Enter key to search: "))
        hash_table.search(key)

    elif choice == '3':
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)

    elif choice == '4':
        hash_table.display()

    elif choice == '5':
        print("Exiting program... 👋")
        break
    else:
        print("Invalid choice! Try again.")
