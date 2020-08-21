N = int(input())
seat = input()
count = 0
result = 1
for i in range(len(seat)):
    if seat[i] == 'L':
        if count % 2 == 1:
            count += 1
        else:
            count += 1
            result += 1
    elif seat[i] == 'S':
        result += 1

if result > N:
    result = N
print(result)