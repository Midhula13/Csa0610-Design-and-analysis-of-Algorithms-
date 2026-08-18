import random
import time

recursive_calls = 0
max_depth = 0

def merge_sort(arr, depth=1):
    global recursive_calls, max_depth

    recursive_calls += 1

    if depth > max_depth:
        max_depth = depth

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

n = int(input("Enter the number of elements: "))

arr = [random.randint(1, 1000) for _ in range(n)]

print("\nOriginal Array:")
print(arr)

start = time.perf_counter()

sorted_arr = merge_sort(arr)

end = time.perf_counter()

print("\nSorted Array:")
print(sorted_arr)

print("\n----- Results -----")
print("Input Size               :", n)
print("Recursive Calls          :", recursive_calls)
print("Maximum Recursion Depth  :", max_depth)
print("Execution Time (ms)      :", round((end - start) * 1000, 5))
