# 1946: 신입 사원

import sys
sys.stdin = open('1946_input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    people.sort()
    min_value = N + 1

    count = 0
    for i in range(N):
        now = people[i]
        # 서류등수는 낮지만 면접등수는 높은 경우
        if now[1] < min_value:
            count += 1
            min_value = now[1]
            # 지금까지 나온 면접등수 중 가장 높은 등수가 2일 경우
            # 이후 등수 중에서는 면접등수가 1인 경우만 카운트될 것이므로
            if min_value == 2:
                count += 1
                break
        
    print(count)