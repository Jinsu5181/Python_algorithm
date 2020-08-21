T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            e = a + dx[k]
            r = b + dy[k]
            if 0 <= e < w and 0 <= r < h and s[e][r] == 1:
                s[e][r] = 0
                queue.append([e, r])


for i in range(T):
    w, h, p = map(int, input().split())
    s = [[0]*h for i in range(w)]
    count = 0
    for j in range(p):
        pos = list(map(int, input().split()))
        s[pos[0]][pos[1]] = 1
    for e in range(w):
        for r in range(h):
            if s[e][r] == 1:
                bfs(e, r)
                s[e][r] = 0
                count += 1
    print(count)