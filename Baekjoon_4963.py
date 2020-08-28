from collections import deque
dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def BFS(c):
    de = deque()
    de.append(c)
    while len(de) != 0:
       c = de.popleft()
       for i in range(8):
           x = c[0] + dx[i]
           y = c[1] + dy[i]
           if 0 <= x < h and 0 <= y < w and board[x][y] == 1:
               board[x][y] = 0
               de.append([x, y])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split()))for i in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                BFS([i, j])

    print(cnt)