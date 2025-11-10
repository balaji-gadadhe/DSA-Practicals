INF = 999999

def prims_algorithm(graph, n):
    selected = [0] * n
    selected[0] = 1  # start from first location
    edges = 0
    total = 0

    print("\nRoutes chosen by pizza boy:")
    while edges < n - 1:
        min_time = INF
        a = 0
        b = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j] != 0:
                        if graph[i][j] < min_time:
                            min_time = graph[i][j]
                            a = i
                            b = j

        print("From Location", a + 1, "to Location", b + 1, "=", graph[a][b], "min")
        total += graph[a][b]
        selected[b] = 1
        edges += 1

    print("\nTotal Minimum Delivery Time =", total, "minutes")


def display_graph(graph):
    print("\nAdjacency Matrix:")
    for row in graph:
        print(row)


def take_input():
    n = int(input("Enter number of locations: "))
    graph = []
    print("Enter adjacency matrix (0 if no direct route):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        graph.append(row)
    return graph, n


def main():
    graph = []
    n = 0
    while True:
        print("\n--- Pizza Delivery Optimization Menu ---")
        print("1. Enter Graph (Adjacency Matrix)")
        print("2. Display Graph")
        print("3. Find Minimum Delivery Time (Prim’s Algorithm)")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            graph, n = take_input()
        elif choice == 2:
            if graph:
                display_graph(graph)
            else:
                print("Graph not entered yet.")
        elif choice == 3:
            if graph:
                prims_algorithm(graph, n)
            else:
                print("Please enter the graph first.")
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
