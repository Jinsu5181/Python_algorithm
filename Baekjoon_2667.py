N = int(input())
board = [list(map(int, input()))for i in range(N)]
# 좌/우/상/하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = []
house = []
count = 0


def bfs(q, w):
    queue = [[q, w]]
    ea = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < N and 0 <= y < N and board[x][y] == 1:
                board[x][y] = 0
                queue.append([x, y])
                ea += 1
    house.append(ea)


for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = 0
            bfs(i, j)
            count += 1
            visit.append(count)
        house.sort()
print(len(visit))
for i in house:
    print(i)