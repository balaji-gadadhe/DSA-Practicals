# Program: Sort Employee Salaries using Selection / Bubble Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def display_top_five(sorted_salaries):
    sal = sorted_salaries[::-1]
    print("Top 5 salaries are:", sal[:5])


# ---------- INPUT ----------
n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    sal = float(input(f"Enter salary of employee {i + 1}: "))
    salaries.append(sal)

print("\n1. Sort using Selection Sort")
print("2. Sort using Bubble Sort")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    selection_sort(salaries)  # sorts the original list
    print("\nSorted Salaries (Selection Sort):", salaries)
    display_top_five(salaries)

elif choice == 2:
    bubble_sort(salaries)  # sorts the original list
    print("\nSorted Salaries (Bubble Sort):", salaries)
    display_top_five(salaries)

else:
    print("Invalid choice!")
