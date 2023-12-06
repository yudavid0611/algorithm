import sys
sys.setrecursionlimit(100000)
sys.stdin = open('1030_input.txt')
input = sys.stdin.readline


def fractal(row, col, len_edge):
    global N, K

    # 시점 0에서는 흰색 사각형 하나만 존재
    if len_edge == 1:
        return 0
    else:
        # K * K 정사각형에 해당하는 범위 구하기
        len_square_edge = len_edge // N * K
        square_start = (len_edge - len_square_edge) // 2
        square_end = square_start + len_square_edge - 1
        
        # 중앙에 위치할 경우
        if square_start <= row <= square_end and square_start <= col<= square_end:
            return 1
        else:
            return fractal(row%(len_edge//N), col%(len_edge//N), len_edge//N)


if __name__ == '__main__':
    S, N, K, R1, R2, C1, C2 = map(int, input().split())

    for r in range(R2 - R1 + 1):
        for c in range(C2 - C1 + 1):
            print(fractal(r + R1, c + C1, N ** S), end='')
        print()