import sys
sys.stdin = open('BOJ/14888/14888_input.txt', 'r')

# idea
# - 백트랙킹

# flow
# 1. 앞쪽 연산자부터 연산자를 차례대로 넣음
# 2. 더 이상 새로운 연산자 조합이 나오지 않을 때까지 진행

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

visited_add = [0] * N - 1
visited_sub = [0] * N - 1
visited_multi = [0] * N - 1
visited_div = [0] * N - 1

while True:
    max_result = -1e9-1
    min_result = 1e9+1
    operator_comb = []
    operator_comb_top = -1

    while not breaking and operator_comb_top < N:
        breaking = False
        operator_comb_top += 1
        for idx, op in enumerate(operators):
            if not op:
                continue
            if idx == 0 and not visited_add[operator_comb_top]:
                operators[idx] -= 1
                visited_add[operator_comb_top] = 1
                operator_comb[operator_comb_top] = '+'
                break
            elif idx == 1 and not visited_add[operator_comb_top]:
                operators[idx] -= 1
                visited_add[operator_comb_top] = 1
                operator_comb[operator_comb_top] = '-'
                break
            elif idx == 2 and not visited_add[operator_comb_top]:
                operators[idx] -= 1
                visited_add[operator_comb_top] = 1
                operator_comb[operator_comb_top] = '*'
                break
            elif idx == 3 and not visited_add[operator_comb_top]:
                operators[idx] -= 1
                visited_add[operator_comb_top] = 1
                operator_comb[operator_comb_top] = '/'
                break
            else:
                breaking = True
                break
        


                