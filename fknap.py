n = int(input("Enter number of items: "))

weight = list(map(int, input("Enter weights: ").split()))
value = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter bag capacity: "))

items = []

for i in range(n):
    ratio = value[i] / weight[i]
    items.append((ratio, weight[i], value[i]))

# Sort according to value/weight ratio
items.sort(reverse=True)

total_value = 0

for ratio, w, v in items:

    if capacity >= w:
        capacity = capacity - w
        total_value = total_value + v

    else:
        total_value = total_value + ratio * capacity
        capacity = 0
        break

print("Maximum value:", total_value)
