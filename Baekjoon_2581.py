m = int(input())
n = int(input())
count = 0
result = []
result_sum = 0
for i in range(m, n+1):
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
        else:
            continue
    if count == 2:
        result.append(i)
        count = 0
    else:
        count = 0

if not result:
    print(-1)
else:
    for j in result:
        result_sum += j
    print(result_sum)
    print(min(result))