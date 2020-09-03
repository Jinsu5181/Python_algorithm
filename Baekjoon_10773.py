K = int(input())
s = []
result = 0
for i in range(K):
    n = int(input())
    if n == 0:
        s.pop()
    else:
        s.append(n)


for j in s:
    result += j

print(result)