# 시간초과: 정답과 무관한 칸의 데이터까지 무수히 생성해야 함

import sys
sys.setrecursionlimit(100000)
sys.stdin = open('1030_input.txt')
input = sys.stdin.readline


def fractal(row, col, color, t):
    global S, N, K, R1, R2, C1, C2, square_start, answer
    '''
    row, col: 현재 칸의 행과 열
    color: False=white, True=black
    t: 현재 진행된 시간
    '''

    # 문제에서 요구하는 시간에 도달한 경우
    if t == S:
        
        # 문제에서 요구하는 구간에 포함된 칸 & color가 black일 경우
        if R1 <= row <= R2 and C1 <= col <= C2 and color == True:
            answer[row - R1][col - C1] = '1'
    
    else:
        # K * K 정사각형에 해당하는 범위 구하기
        square_r1 = N * row + square_start
        square_r2 = square_r1 + K - 1
        square_c1 = N * col + square_start
        square_c2 = square_c1 + K - 1

        for i in range(N):
            for j in range(N):
                next_row = N * row + i
                next_col = N * col + j

                # 현재 색이 black일 경우
                if color == True:
                    fractal(next_row, next_col, color, t + 1)
                
                # 현재 색이 white일 경우
                else:
                    # K * K 정사각형에 포함될 경우
                    if square_r1 <= next_row <= square_r2 and square_c1 <= next_col <= square_c2:
                        fractal(next_row, next_col, not color, t + 1)
                    else:
                        fractal(next_row, next_col, color, t + 1)


if __name__ == '__main__':
    S, N, K, R1, R2, C1, C2 = map(int, input().split())
    answer = [['0'] * (C2 - C1 + 1) for _ in range(R2 - R1 + 1)]
    square_start = (N - K) // 2
    fractal(0, 0, False, 0)
    for r in answer:
        print(''.join(r))