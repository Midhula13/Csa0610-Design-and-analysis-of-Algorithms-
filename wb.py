text = input("Enter a word: ")

dictionary = input("Enter dictionary words separated by space: ").split()

n = len(text)

dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for word in dictionary:
        if text[i - len(word):i] == word and dp[i - len(word)]:
            dp[i] = True

if dp[n]:
    print("Word can be broken")
else:
    print("Word cannot be broken")
