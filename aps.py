n = int(input("Enter number of vertices: "))

print("Enter cost matrix:")
print("Use 999 for infinity")

distance = []

for i in range(n):
    row = list(map(int, input().split()))
    distance.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):

            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

print("Shortest distance matrix:")

for row in distance:
    print(row)
