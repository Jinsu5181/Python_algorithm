N = int(input())
price = []
for i in range(N):
    price.append(list(map(int, input().split())))

for j in range(1, len(price)):
    price[j][0] = min(price[j - 1][1], price[j - 1][2]) + price[j][0]
    price[j][1] = min(price[j - 1][0], price[j - 1][2]) + price[j][1]
    price[j][2] = min(price[j - 1][0], price[j - 1][1]) + price[j][2]

print(min(price[N - 1][0], price[N - 1][1], price[N - 1][2]))