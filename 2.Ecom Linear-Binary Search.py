# 🛒 E-Commerce Customer Account Search (Menu Driven + Functions)

# --- Functions Section ---

def input_customer_ids():
    n = int(input("Enter number of customer IDs: "))
    ids = []
    for i in range(n):
        cid = int(input(f"Enter customer ID {i+1}: "))
        ids.append(cid)
    return ids

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # found
    return -1           # not found

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def display_ids(arr):
    print("Current Customer IDs:", arr)


# --- Main Program ---
customer_ids = []

while True:
    print("\n===== E-COMMERCE MENU =====")
    print("1. Enter Customer IDs")
    print("2. Display Customer IDs")
    print("3. Linear Search")
    print("4. Binary Search (on sorted list)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1️⃣ Enter IDs
    if choice == '1':
        customer_ids = input_customer_ids()
        print("✅ Customer IDs added successfully!")

    # 2️⃣ Display IDs
    elif choice == '2':
        if len(customer_ids) == 0:
            print("⚠️ No customer IDs available!")
        else:
            display_ids(customer_ids)

    # 3️⃣ Linear Search
    elif choice == '3':
        if len(customer_ids) == 0:
            print("⚠️ Please enter customer IDs first!")
        else:
            key = int(input("Enter Customer ID to search: "))
            pos = linear_search(customer_ids, key)
            if pos != -1:
                print(f"✅ (Linear Search) Customer ID {key} found at position {pos}")
            else:
                print(f"❌ (Linear Search) Customer ID {key} not found")

    # 4️⃣ Binary Search
    elif choice == '4':
        if len(customer_ids) == 0:
            print("⚠️ Please enter customer IDs first!")
        else:
            key = int(input("Enter Customer ID to search: "))
            sorted_ids = sorted(customer_ids)
            pos = binary_search(sorted_ids, key)
            if pos != -1:
                print(f"✅ (Binary Search) Customer ID {key} found at position {pos} (in sorted list)")
            else:
                print(f"❌ (Binary Search) Customer ID {key} not found (in sorted list)")

    # 5️⃣ Exit
    elif choice == '5':
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")
