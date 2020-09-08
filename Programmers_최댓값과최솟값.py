def solution(s):
    answer = ''
    arr = [int(x) for x in s.split()]
    print(arr)
    max_num = max(arr)
    min_num = min(arr)
    answer = str(min(arr))+' '+str(max(arr))
    return answer