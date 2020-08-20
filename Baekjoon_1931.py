N = int(input())
t = []
end = 0
count = 0
for i in range(N):
    s, e = map(int, input().split())
    t.append([s, e])

t = sorted(t, key=lambda a: a[0])
t = sorted(t, key=lambda a: a[1])

for i, j in t:
    if i >= end:
        count += 1
        end = j

print(count)

