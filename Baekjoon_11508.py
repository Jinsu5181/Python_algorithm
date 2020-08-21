N = int(input())
price_menu = []
result = 0
for i in range(N):
    price = int(input())
    price_menu.append(price)

price_menu.sort(reverse=True)

for j in range(N):
    if (j % 3) != 2:
        result += price_menu[j]
print(result)
