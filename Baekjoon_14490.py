from math import gcd
s = input().split(':')
arr = []
r = []
for i in s:
    arr.append(int(i))
num = gcd(arr[0], arr[1])
for i in arr:
    r.append(str(i//num))

print(':'.join(r))