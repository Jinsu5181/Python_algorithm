from collections import deque
import sys
N = int(input())
qu = deque([])
for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        qu.append(com[1])
    elif com[0] == 'pop':
        if not qu:
            print(-1)
        else:
            print(qu.popleft())
    elif com[0] == 'size':
        print(len(qu))
    elif com[0] == 'empty':
        if not qu:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not qu:
            print(-1)
        else:
            print(qu[0])
    elif com[0] == 'back':
        if not qu:
            print(-1)
        else:
            print(qu[-1])