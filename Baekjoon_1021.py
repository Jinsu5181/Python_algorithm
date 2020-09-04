from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
pos = list(map(int, input().split()))
q = deque([])
cnt = 0
count = 0
for i in range(1, N+1):
    q.append(i)

for j in range(M):
    if q.index(pos[j]) < len(q) - q.index(pos[j]):
        while True:
            if q[0] == pos[j]:
                q.popleft()
                break
            else:
                q.append(q[0])
                q.popleft()
                cnt += 1
    else:
        while True:
            if q[0] == pos[j]:
                q.popleft()
                break
            else:
                q.appendleft(q[-1])
                q.pop()
                cnt += 1
print(cnt)
