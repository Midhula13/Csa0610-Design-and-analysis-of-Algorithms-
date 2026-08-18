n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times: ").split()))
finish = list(map(int, input("Enter finish times: ").split()))

activities = list(zip(start, finish))
activities.sort(key=lambda x: x[1])

count = 1
last_finish = activities[0][1]

for i in range(1, n):
    if activities[i][0] >= last_finish:
        count += 1
        last_finish = activities[i][1]

print("Max Activities =", count)
