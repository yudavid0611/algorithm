import sys
from collections import defaultdict

sys.stdin = open('1005_input.txt')
sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times= list(map(int, sys.stdin.readline().split()))
    
    # 건물 인덱스와 맞추기 위해 앞에 0 추가
    times = [0] + times

    order = defaultdict(list)
    for _ in range(K):
        bef, aft = map(int, sys.stdin.readline().split())
        order[aft].append(bef)

    W = int(input())

    # 건물 번호와 맞추기 위해 N + 1개만큼 생성
    # memo: 해당 인덱스 건물을 짓기 위해 필요한 최소 시간
    memo = [-1] * (N + 1)

    def get_time(structure):
        # 이미 최소 시간이 계산된 건물인 경우
        if memo[structure] != -1:
            return memo[structure]
        else:
            # 해당 건물을 짓기 위해 사전에 지어져야 할 건물이 없는 경우
            if not order[structure]:
                memo[structure] = times[structure]
            # 해당 건물을 짓기 위해 사전에 지어져야 할 건물이 있는 경우
            else:
                time = times[structure] + max(map(get_time, order[structure]))
                memo[structure] = time
            return memo[structure]

    print(get_time(W))