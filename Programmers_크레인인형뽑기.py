def solution(board, moves):
    q = []
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                q.append(board[j][i-1])
                board[j][i-1] = 0
                if q[-1:] == q[-2:-1]:
                    basket += q[-1:]
                    q = q[:-2]
                break
    return len(basket)*2