#Library management

members={}
books={}

def add_member():
    name=input("enter name")
    books_borrowed=int(input("no of books borrowed"))
    members[name]=books_borrowed
    print("member added")

def add_book():
    book_name = input("Enter book name: ")
    times_borrowed = int(input("Enter number of times borrowed: "))
    books[book_name] = times_borrowed
    print("Book record added successfully!")

def avg_books():
    if len(members)==0:
        print("No members")
        return
    total = 0
    for books_borrowed in members.values():
        total += books_borrowed   
    avg=total/len(members)
    print("Avg books borrowed: ", avg)

def book_high_low():
    if len(books) == 0:
        print("No books found!")
        return
    # get first key manually using a loop
    for k in books:
        max_book = k
        min_book = k
        break  # stop after first key
    # now compare all keys
    for book in books:
        if books[book] > books[max_book]:
            max_book = book
        if books[book] < books[min_book]:
            min_book = book
    print("🏆 Highest borrowed book:", max_book, "->", books[max_book])
    print("📉 Lowest borrowed book:", min_book, "->", books[min_book])

def count_zero_borrowers():
    count = 0
    for value in members.values():
        if value == 0:
            count += 1
    print("🙅 Members who borrowed 0 books:", count)

def most_frequent_book():
    if len(books) == 0:
        print("⚠️ No books found!")
        return
    # get first key manually
    for k in books:
        max_count = books[k]
        break
    # find the highest count manually
    for book in books:
        if books[book] > max_count:
            max_count = books[book]
    # now find all books having that max_count
    most_borrowed = []
    for book in books:
        if books[book] == max_count:
            most_borrowed.append(book)

    print("🔥 Most borrowed book(s):", most_borrowed, "->", max_count, "times")

def display_all():
    print("\n--- 👤 Members ---")
    if len(members) == 0:
        print("No members yet!")
    else:
        for name, count in members.items():
            print(name, ":", count)

    print("\n--- 📚 Books ---")
    if len(books) == 0:
        print("No books yet!")
    else:
        for book, count in books.items():
            print(book, ":", count)

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Member")
    print("2. Add Book")
    print("3. Show Average Books Borrowed")
    print("4. Show Highest and Lowest Borrowed Books")
    print("5. Count Members with 0 Borrowings")
    print("6. Show Most Borrowed Book")
    print("7. Display All Data")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_member()
    elif choice == '2':
        add_book()
    elif choice == '3':
        avg_books()
    elif choice == '4':
        book_high_low()
    elif choice == '5':
        count_zero_borrowers()
    elif choice == '6':
        most_frequent_book()
    elif choice == '7':
        display_all()
    elif choice == '8':
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")
