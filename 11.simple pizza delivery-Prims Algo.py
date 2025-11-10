INF = 9999999

# Number of locations
n = 5

# Adjacency matrix (0 means no route)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * n
selected[0] = True   # start from location 1
edges = 0
total_time = 0

print("Selected routes:")

while edges < n - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if (not selected[j]) and graph[i][j]:
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(f"Location {x+1} --> Location {y+1} : {graph[x][y]} min")
    total_time += graph[x][y]
    selected[y] = True
    edges += 1

print("\nTotal Minimum Delivery Time:", total_time, "minutes")
