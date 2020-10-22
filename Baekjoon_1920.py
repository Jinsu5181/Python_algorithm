def binary_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return arr[mid]

    elif arr[mid] >= target:
        return binary_search(arr, start, mid-1, target)

    else:
        return binary_search(arr, mid+1, end, target)

    return None

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

arr.sort()

for i in chk:
    result = binary_search(arr, 0, n-1, i)

    if result == None:
        print(0)
    else:
        print(1)