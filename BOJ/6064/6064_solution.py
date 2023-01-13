# 6064: 카잉 달력

# M - x -> 초기값, 그 이후로는 M씩 더해야 함
# N - y -> 초기값, 그 이후로는 N씩 더해야 함

import sys
from collections import defaultdict
sys.stdin = open('6064_input.txt')

T = int(input())

year2_visited = defaultdict(int)

for _ in range(T):
    M, N, X, Y = list(map(int, input().split()))
    success = False
    idx = X - 1
    # year1 = idx + 1
    year2 = 1 + idx
    if year2 > N:
        year2 = year2 % N

    while True:
        if type(year2_visited.get(year2)) == int:
            year2_visited[year2] += 1
            print(year2_visited)
            if len(set(year2_visited.items())) == 1:
                break
        else:
            year2_visited[year2]
            print(year2_visited)
        if year2 == Y:
            success = True
            break
        elif year2 == N:
            break
        
        idx += M
        year2 += M
        if year2 > N:
            year2 = year2 % N
        # print(idx, year2)
    if success:
        print(idx + 1)
    else:
        print(-1)

    # const1 = X - 1
    # const2 = Y - 1

    # year1 = []
    # year2 = []

    # idx = 0
    # success = False
    # result = -2
    # year1_now = 1
    # year2_now = 1
    # # year2_break = False
    # while True:
    #     if year1_now == M and year2_now == N:
    #         break

        
    #     # 첫 번째 연도
    #     year1_next = const1 + M * idx
    #     year2_next = const2 + N * idx

    #     if M >= N:
    #         if year2_next in year1:
    #             result = year2_next
    #             success = True
    #             break
    #         year1.append(year1_next)
    #     else:
    #         if year1_next in year2:
    #             result = year1_next
    #             success = True
    #             break
    #         year2.append(year2_next)
    #     idx += 1

    #     print(year1, year2, idx)
    # # if year1_break:
    # #     while True:
    # #         year2_next = const2 + N * idx
    # #         if year2_next >= N:
    # #             break
    # #         year2.append(year2_next)
    # # else:
    # #     idx += 1
    # #     while True:
    # #         year1_next = const1 + M * idx
    # #         if year1_next >= M:
    # #             break
    # #         year1.append(year1_next)
    # print(year1)
    # print(year2)
    # if success != -2:
    #     print(result + 1)
    # else:
    #     print(-1)

