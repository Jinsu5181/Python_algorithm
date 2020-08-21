N, M = map(int, input().split())  # 크기 입력
visit = [list(map(int, input())) for i in range(N)]  # 미로 입력
queue = []

visit[0][0] = 1
queue = [[0, 0]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and visit[x][y] == 1:
            queue.append([x, y])
            visit[x][y] = visit[a][b] + 1

print(visit[N-1][M-1])