# ---------------- DFS using Adjacency Matrix ----------------
def dfs(matrix, start, visited, locations):
    print(locations[start], end=" ")
    visited[start] = True
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited, locations)

# ---------------- BFS using Adjacency List ----------------
def bfs(graph, start, locations):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(locations[node], end=" ")
        for neighbour in graph[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

# ---------------- MAIN ----------------
def main():
    # Locations
    locations = ['A', 'B', 'C', 'D', 'E']

    # ---------- Adjacency Matrix for DFS ----------
    matrix = [
        [0, 1, 1, 0, 0],  # A connected to B, C
        [1, 0, 0, 1, 0],  # B connected to A, D
        [1, 0, 0, 1, 1],  # C connected to A, D, E
        [0, 1, 1, 0, 0],  # D connected to B, C
        [0, 0, 1, 0, 0]   # E connected to C
    ]

    print("DFS Traversal (Adjacency Matrix): ", end="")
    visited = [False] * len(matrix)
    dfs(matrix, 0, visited, locations)  # Start from A
    print("\n")

    # ---------- Adjacency List for BFS ----------
    graph = [
        [1, 2],     # A -> B, C
        [0, 3],     # B -> A, D
        [0, 3, 4],  # C -> A, D, E
        [1, 2],     # D -> B, C
        [2]         # E -> C
    ]

    print("BFS Traversal (Adjacency List): ", end="")
    bfs(graph, 0, locations)  # Start from A
    print()

# Run program
main()
