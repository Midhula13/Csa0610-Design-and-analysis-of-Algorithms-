n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

distance = [float('inf')] * n
distance[source] = 0

for i in range(n - 1):

    for u, v, w in edges:

        if distance[u] != float('inf'):
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

print("Shortest distances:")

for i in range(n):
    print("Vertex", i, ":", distance[i])
