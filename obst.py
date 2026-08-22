n = int(input("Enter number of keys: "))

frequency = list(map(int, input("Enter frequencies: ").split()))

dp = [[0] * n for i in range(n)]

for i in range(n):
    dp[i][i] = frequency[i]

for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1

        total = sum(frequency[i:j + 1])

        dp[i][j] = float('inf')

        for root in range(i, j + 1):

            left = 0
            right = 0

            if root > i:
                left = dp[i][root - 1]

            if root < j:
                right = dp[root + 1][j]

            cost = left + right + total

            if cost < dp[i][j]:
                dp[i][j] = cost

print("Minimum OBST cost:", dp[0][n - 1])
