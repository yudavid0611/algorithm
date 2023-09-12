import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('12100_input.txt')
input = sys.stdin.readline

# 각 블럭을 움직이는 함수
def move_block(row, col, new_board, d, combined):
    global max_number
    global is_moved

    # 해당 칸에 블록이 없을 경우
    if new_board[row][col] == 0:
        return 
    
    while True:
        new_row, new_col = row + d[0], col + d[1]

        # 이동하려는 칸이 유효한 범주에 있는지 확인
        if 0 <= new_row < N and 0 <= new_col < N:
            
            # 해당 위치에 블록이 있을 경우
            if new_board[new_row][new_col] != 0:
                
                # 이미 합쳐진 블록인 경우
                if combined[new_row][new_col] == 1:
                    break
                
                # 합쳐진 블록이 아닌 경우
                else:
                    # 두 수가 같으면 합치기
                    if new_board[new_row][new_col] == new_board[row][col]:
                        new_board[new_row][new_col] *= 2
                        new_board[row][col] = 0
                        combined[new_row][new_col] = 1
                        
                        # 최대값 경신
                        if max_number < new_board[new_row][new_col]:
                            max_number = new_board[new_row][new_col]
                        is_moved = True
                    break
            
            # 해당 위치에 블록이 없을 경우
            else:
                # 이동
                new_board[new_row][new_col] = new_board[row][col]
                new_board[row][col] = 0

                row, col = new_row, new_col

                is_moved = True
                
        # 유효한 범주에 없을 경우       
        else:
            break


# board를 움직이는 함수
def shake_board(queue):
    global is_moved

    while queue:

        now_board, n_try = queue.popleft()

        ## 상 ##
        new_board = deepcopy(now_board)

        # 합쳐진 블록 체크
        combined = [[0] * N for _ in range(N)]
        
        is_moved = False
        
        for i in range(N):
            for j in range(N):
                move_block(i, j, new_board, delta[0], combined)

        if is_moved and n_try < 4:
            queue.append([new_board, n_try + 1])
        
        
        ## 우 ##
        new_board = deepcopy(now_board)

        # 합쳐진 블록 체크
        combined = [[0] * N for _ in range(N)]
        
        is_moved = False

        for i in range(N - 1, -1, -1):
            for j in range(N):
                move_block(j, i, new_board, delta[1], combined)

        if is_moved and n_try < 4:
            queue.append([new_board, n_try + 1])


        ## 하 ##
        new_board = deepcopy(now_board)

        # 합쳐진 블록 체크
        combined = [[0] * N for _ in range(N)]
        
        is_moved = False

        for i in range(N - 1, -1, -1):
            for j in range(N):
                move_block(i, j, new_board, delta[2], combined)

        if is_moved and n_try < 4:
            queue.append([new_board, n_try + 1])


        ## 좌 ##
        new_board = deepcopy(now_board)

        # 합쳐진 블록 체크
        combined = [[0] * N for _ in range(N)]

        is_moved = False

        for i in range(N):
            for j in range(N):
                move_block(j, i, new_board, delta[3], combined)

        if is_moved and n_try < 4:
            queue.append([new_board, n_try + 1])


if __name__ == '__main__':
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    queue.append([board, 0])

    # 상, 우, 하, 좌 방향
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # 최대값 초기화
    max_number = 0
    for i in range(N):
        for j in range(N):
            if max_number < board[i][j]:
                max_number = board[i][j]

    # 움직인 블럭이 있는지 체크할 변수 초기화
    is_moved = False
    
    shake_board(queue)

    print(max_number)