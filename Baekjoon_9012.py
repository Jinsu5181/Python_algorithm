T = int(input())
for i in range(T):
    pl = 0
    A = input()
    s = list(A)
    for j in s:
        if j == '(':
            pl += 1
        elif j == ')':
            pl -= 1
        if pl < 0:
            print('NO')
            break
    if pl > 0:
        print('NO')
    elif pl == 0:
        print('YES')