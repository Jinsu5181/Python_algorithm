from collections import deque
import sys
N = int(sys.stdin.readline())
q = deque([])
for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        q.appendleft(com[1])
    elif com[0] == 'push_back':
        q.append(com[1])
    elif com[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    elif com[0] == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q[-1])
            q.pop()
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])