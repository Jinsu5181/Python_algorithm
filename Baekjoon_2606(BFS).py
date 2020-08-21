com = int(input())
connect = int(input())
s = [[0] * (com + 1) for i in range(com + 1)]
for i in range(connect):
    line = list(map(int, input().split()))
    s[line[0]][line[1]] = 1
    s[line[1]][line[0]] = 1


def bfs(start):
    visit = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for i in range(len(s[start])):
            if s[node][i] == 1 and (i not in visit):
                visit.append(i)
                queue.append(i)
    return len(visit) - 1

print(bfs(1))