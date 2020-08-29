from collections import deque


def BFS(k):
    q = deque()
    visit = [False]*(n+1)
    q.append(k)
    visit[k] = True
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            k = q.popleft()
            if k == end:
                return cnt - 1
            for j in adj[k]:
                if not (visit[j]):
                    visit[j] = True
                    q.append(j)
    return -1


n = int(input())
start, end = map(int, input().split())
m = int(input())
adj = [[]for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(BFS(start))