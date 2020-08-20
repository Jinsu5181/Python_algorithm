import sys

N = int(sys.stdin.readline())

sor = []
for i in range(N):
    A = int(sys.stdin.readline())
    sor.append(A)

sor.sort()

for i in range(N):
    print(sor[i])