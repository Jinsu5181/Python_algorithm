i = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        i += 1
        if P < V:
            A = (V // P)*L
            if V % P < L:
                B = V % P
            else:
                B = L
    print("Case %d: "%i, end='')
    print(A + B)