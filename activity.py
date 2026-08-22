n = int(input("Enter number of activities: "))

start = []
finish = []

for i in range(n):
    s = int(input("Enter start time: "))
    f = int(input("Enter finish time: "))
    start.append(s)
    finish.append(f)

# Sort activities according to finish time
activities = list(zip(start, finish))
activities.sort(key=lambda x: x[1])

selected = []
last_finish = 0

for s, f in activities:
    if s >= last_finish:
        selected.append((s, f))
        last_finish = f

print("Selected activities:")
for activity in selected:
    print(activity)
