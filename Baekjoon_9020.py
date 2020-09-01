p = 10000
flag = [True] * 10000

for i in range(2, 100):
    for j in range(2 * i, 10000, i):
        flag[j] = False

T = int(input())
for i in range(T):
    n = int(input())
    m = n // 2
    for j in range(m, 1, -1):
        if flag[n - j] and flag[j]:
            print(j, n - j)
            break