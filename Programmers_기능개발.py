import math


def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-x)/y) for x, y in zip(progresses, speeds)]
    cnt = 0
    for i in range(len(progresses)):
        if progresses[cnt] < progresses[i]:
            answer.append(i-cnt)
            cnt = i
    answer.append(len(progresses)-cnt)

    return answer