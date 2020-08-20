T = int(input())
if (T % 10) != 0:
    print(-1)
else:
    if T >= 300:
        A = T // 300
        B = (T % 300) // 60
        C = (T % 60) // 10
    elif T < 300:
        A = 0
        B = T // 60
        C = (T % 60) // 10
    elif T < 60:
        A = 0
        B = 0
        C = T // 10

    print("{0} {1} {2}".format(A, B, C))