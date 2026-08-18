A = []
B = []

for i in range(2):
    A.append(list(map(int, input().split())))

for i in range(2):
    B.append(list(map(int, input().split())))

a, b = A[0]
c, d = A[1]

e, f = B[0]
g, h = B[1]

M1 = (a + d) * (e + h)
M2 = (c + d) * e
M3 = a * (f - h)
M4 = d * (g - e)
M5 = (a + b) * h
M6 = (c - a) * (e + f)
M7 = (b - d) * (g + h)

C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6

print(C11, C12)
print(C21, C22)
