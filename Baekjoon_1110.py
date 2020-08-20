N = int(input())
count = 0
result = N
while True:
    A = result // 10
    B = result % 10
    C = A + B
    result = (B * 10)+(C % 10)
    count += 1
    if result == N:
        break

print(count)