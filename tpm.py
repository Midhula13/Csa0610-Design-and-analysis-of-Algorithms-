text = input("Enter text: ")
pattern = input("Enter pattern: ")

n = len(text)
m = len(pattern)

found = False

for i in range(n - m + 1):

    match = True

    for j in range(m):

        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        print("Pattern found at position:", i)
        found = True

if not found:
    print("Pattern not found")
