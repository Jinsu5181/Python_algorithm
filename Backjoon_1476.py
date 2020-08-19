E, S, M = map(int, input().split())
Y = 1
a, b, c = 1, 1, 1
while True:
    if a == E and b == S and c == M:
        break
    if a >= 15:
        a -= 15
    if b >= 28:
        b -= 28
    if c >= 19:
        c -= 19

    a += 1
    b += 1
    c += 1

    Y += 1
print(Y)