import sys
sys.stdin = open('10830_input.txt')

# 행렬곱 함수
def matmul(a, b, d=1000):
    row_len = len(a)
    col_len = len(b[0])
    result = [[0] * col_len for _ in range(row_len)]

    a_col_len = len(a[0])
    for r in range(row_len):
        for c in range(col_len):
            v = 0
            for i in range(a_col_len):
                v += a[r][i] * b[i][c]
            
            # v mod d를 결과값으로 넣어주어 추후 연산 크기를 줄여줌
            result[r][c] = v % d
    return result

# 분할정복
def div_con(a, n, e):
    # n==1일 경우 항등함수와 곱해줌
    if n == 1:
        return matmul(a, e)
    else:
        # n이 짝수일 경우
        if n % 2 == 0:
            mat = div_con(a, n//2, e)
            mat = matmul(mat, mat)
            
        # n이 홀수일 경우
        else:
            mat = div_con(a, (n-1)//2, e)
            mat = matmul(mat, mat)
            mat = matmul(mat, a)
            
    return mat

N, B = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 항등함수 만들기
E = [[0] * len(A[0]) for _ in range(len(A))]
for i in range(len(E)):
    E[i][i] = 1

result = div_con(A, B, E)
for i in range(len(result)):
    print(' '.join(map(str, result[i])))