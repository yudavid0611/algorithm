import sys
sys.stdin = open('1932_input.txt')

## 접근법 ##
# 1. 각 칸마다의 최대값을 저장한다.
#   이전 칸의 왼쪽, 오른쪽 값 중 더 큰 값에 현재 칸의 수를 더하여 구한다.

input_dict = {}
max_dict = {}
n = int(input())

for i in range(n):
    input_dict[i] = list(map(int, sys.stdin.readline().split()))
    max_dict[i] = [0] * (i + 1)

max_dict[0] = input_dict[0]

for row in range(1, n):
    col = 0

    while col <= row:
        # 첫 번째 원소일 경우
        if not col:
            # 이전 행 첫 번째 원소 값에 현재 값 더하기
            max_dict[row][col] = max_dict[row-1][col] + input_dict[row][col]
        
        # 마지막 원소일 경우
        elif col == row:
            # 이전 행 마지막 원소 값에 현재 값 더하기
            max_dict[row][col] = max_dict[row-1][col-1] + input_dict[row][col]
            
        else:
            # 이전 행의 왼쪽 위, 오른쪽 위 값 중 최대값과 현재 값 더하기
            max_dict[row][col] = max(max_dict[row-1][col], max_dict[row-1][col-1]) + input_dict[row][col]

        col += 1

print(max(max_dict[n-1]))