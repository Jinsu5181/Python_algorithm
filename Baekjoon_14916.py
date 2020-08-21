N = int(input())
count = 0
if N % 5 == 0:
    count = N // 5
    print(count)
else:
    while N != 0:
        N -= 2
        count += 1
        if N % 5 == 0:
            count += N // 5
            print(count)
            break
        if N < 0:
            print(-1)
            break