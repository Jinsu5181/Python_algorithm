S = input()
count = 1

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        count += 1

result = count // 2

print(result)