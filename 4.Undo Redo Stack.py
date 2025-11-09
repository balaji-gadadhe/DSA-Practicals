# ------------------ MANUAL STACK VERSION ------------------
undo_stack = []   # Undo stack
undo_top = -1

redo_stack = []   # Redo stack
redo_top = -1

document = ""  # Current document

# ------------------ PUSH -------------------
def push(stack, top, value):
    top = top + 1
    stack[top] = value
    return top

# ------------------ POP --------------------
def pop(stack, top):
    value = stack[top]
    top = top - 1
    return value, top

# ------------------ EDITOR FUNCTIONS -------------------
def make_change(change):
    global document, undo_top, redo_top
    undo_top = push(undo_stack, undo_top, document)  # save current state
    document += change
    redo_top = -1  # clear redo stack
    print("\n✅ Change made:", change)

def undo_action():
    global document, undo_top, redo_top
    if undo_top == -1:
        print("\n⚠️ Nothing to undo.")
        return
    redo_top = push(redo_stack, redo_top, document)  # save current for redo
    document, undo_top = pop(undo_stack, undo_top)   # revert
    print("\n↩️ Undo performed.")

def redo_action():
    global document, undo_top, redo_top
    if redo_top == -1:
        print("\n⚠️ Nothing to redo.")
        return
    undo_top = push(undo_stack, undo_top, document)  # save current for undo
    document, redo_top = pop(redo_stack, redo_top)   # reapply
    print("\n🔁 Redo performed.")

def display_document():
    print("\n📄 Current Document State:", document if document else "(empty)")

# ------------------ MENU -------------------
while True:
    print("\n====== TEXT EDITOR MENU ======")
    print("1. Make a Change")
    print("2. Undo Last Change")
    print("3. Redo Last Change")
    print("4. Display Document")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        change = input("Enter text to add: ")
        make_change(change)
    elif choice == '2':
        undo_action()
    elif choice == '3':
        redo_action()
    elif choice == '4':
        display_document()
    elif choice == '5':
        print("\n👋 Exiting Text Editor... Goodbye!")
        break
    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 5.")
