INF = 999999

# Number of locations
n = 5

# Adjacency Matrix (0 means no direct route)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [0] * n
selected[0] = 1  # start from location 1

edges = 0
total = 0

print("Routes chosen by pizza boy:")

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

    print("From Location", a+1, "to Location", b+1, "=", graph[a][b], "min")
    total += graph[a][b]
    selected[b] = 1
    edges += 1

print("\nTotal Minimum Delivery Time =", total, "minutes")
