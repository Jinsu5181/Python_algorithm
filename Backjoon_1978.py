N = int(input())
num = list(map(int, input().split()))
count = 0
result = 0
for i in num:
    if i == 1:
        continue
    else:
        for j in range(1, i+1):
            if i % j == 0:
                count += 1

    if count == 2:
        result += 1
        count = 0
    else:
        count = 0

print(result)
