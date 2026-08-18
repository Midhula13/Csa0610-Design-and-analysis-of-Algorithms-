a = [[4, 5, 3, 2, 6],
     [2, 10, 1, 4, 8]]

t = [[7, 9, 3, 4, 8],
     [6, 5, 2, 7, 3]]

e = [1, 2]
x = [2, 3]

n = len(a[0])

f1 = e[0] + a[0][0]
f2 = e[1] + a[1][0]

for j in range(1, n):
    f1_old = f1
    f2_old = f2

    f1 = min(f1_old + a[0][j],
             f2_old + t[1][j] + a[0][j])

    f2 = min(f2_old + a[1][j],
             f1_old + t[0][j] + a[1][j])

answer = min(f1 + x[0], f2 + x[1])

print("Minimum time:", answer)
