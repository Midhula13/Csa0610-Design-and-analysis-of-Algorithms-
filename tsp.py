n = int(input("Enter number of cities: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

visited = [False] * n
visited[0] = True

min_cost = float('inf')

def tsp(city, count, total):
    global min_cost

    if count == n:
        total = total + cost[city][0]
        if total < min_cost:
            min_cost = total
        return

    for next_city in range(n):
        if not visited[next_city]:
            visited[next_city] = True

            tsp(next_city, count + 1,
                total + cost[city][next_city])

            visited[next_city] = False

tsp(0, 1, 0)

print("Minimum travelling cost:", min_cost)
