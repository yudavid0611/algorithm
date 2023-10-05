# 10%에서 시간초과. bags.pop(idx)을 매번 수행하는 과정에서 시간이 많이 소요된다.

import sys
from bisect import bisect_left
from collections import deque
sys.stdin = open('1202_input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

jewel = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input().rstrip()) for _ in range(K)]

key = lambda x:x[1]
jewel = sorted(jewel, key=key, reverse=True)
bags = sorted(bags)

price = 0

for w, v in jewel:
    idx = bisect_left(bags, w)

    # 유효한 인덱스일 경우
    if idx < len(bags):
        # 해당 인덱스의 가방에 보석을 넣고 가방은 bags에서 제거
        price += v
        bags.pop(idx)

        # 더 이상 사용 가능한 가방이 없을 경우 break
        if not bags:
            break

print(price)