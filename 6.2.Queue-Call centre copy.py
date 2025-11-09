# ----------------- CALL CENTER QUEUE SIMULATION -----------------

MAX = 50
call_queue = [None] * MAX
front = -1
rear = -1

# ----------------- MANUAL PUSH & POP -----------------
def push(queue, rear, item):
    rear += 1
    queue[rear] = item
    return rear

def pop(queue, front, rear):
    if front == -1 or front > rear:  # queue empty
        return None, front
    item = queue[front]
    front += 1
    if front > rear:  # reset queue if empty
        front = rear = -1
    return item, front

# ----------------- FUNCTION DEFINITIONS -----------------
def addCall():
    global front, rear
    customerID = input("Enter Customer ID: ")
    callTime = input("Enter Call Time (in minutes): ")
    call = (customerID, callTime)
    if front == -1:  # first element
        front = 0
    rear = push(call_queue, rear, call)
    print(f"✅ Call from Customer {customerID} added to the queue.")

def answerCall():
    global front, rear
    call, front = pop(call_queue, front, rear)
    if call is None:
        print("📭 No calls to answer.")
    else:
        print(f"📞 Answered call from Customer {call[0]} (Call time: {call[1]} min).")

def viewQueue():
    if front == -1 or front > rear:
        print("📭 No pending calls in the queue.")
        return
    print("\n📋 Pending Calls in Queue:")
    for i in range(front, rear + 1):
        print(f" Customer ID: {call_queue[i][0]}, Call Time: {call_queue[i][1]} min")

def isQueueEmpty():
    if front == -1 or front > rear:
        print("✅ Queue is empty.")
    else:
        print("❌ Queue is not empty. Total calls in queue:", rear - front + 1)

# ----------------- MENU -----------------
while True:
    print("\n====== CALL CENTER MENU ======")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        addCall()
    elif choice == '2':
        answerCall()
    elif choice == '3':
        viewQueue()
    elif choice == '4':
        isQueueEmpty()
    elif choice == '5':
        print("\n👋 Exiting Call Center System...")
        break
    else:
        print("❌ Invalid choice! Please enter 1 to 5.")
