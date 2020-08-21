com = int(input())
connect = int(input())
s = [[0] * (com + 1) for i in range(com + 1)]
for i in range(connect):
    line = list(map(int, input().split()))
    s[line[0]][line[1]] = 1
    s[line[1]][line[0]] = 1


def dfs(start, visit):
    visit += [start]
    for i in range(len(s[start])):
        if s[start][i] == 1 and (i not in visit):
            dfs(i, visit)
    return len(visit) - 1


print(dfs(1, []))