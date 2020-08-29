t = int(input())

for i in range(t):
    p0 = [1, 0]
    p1 = [0, 1]
    n = int(input())
    if n <= 40:
        for j in range(2, n+1):
            p0.append(p0[j-2]+p0[j-1])
            p1.append(p1[j-2]+p1[j-1])
        print("%d %d"%(p0[n], p1[n]))