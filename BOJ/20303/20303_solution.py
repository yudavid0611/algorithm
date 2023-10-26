import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
sys.stdin = open('20303_input.txt')
input = sys.stdin.readline

# 친구 집합마다의 사람수, 사탕수를 구하는 함수
def dfs(n):
    global num_friends, num_candies
    
    visited[n] = 1
    num_friends += 1
    num_candies += candies[n]

    for friend in friends[n]:
        if visited[friend] == 0:
            dfs(friend)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    candies = [0] + list(map(int, input().split()))
    
    # 친구 관계 그래프
    friends = defaultdict(list)

    cnt_M = 0
    for i in range(1, N + 1):
        friends[i]
        if cnt_M < M:
            a, b = map(int, input().split())
            friends[a].append(b)
            friends[b].append(a)
            cnt_M += 1
    
    # 아직 처리하지 못한 친구관계가 남아 있을 경우
    while cnt_M < M:
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
        cnt_M += 1

    visited = [0] * (N + 1)
    friends_set = []
    for friend in friends:
        # 이미 친구 관계가 맺어진 경우
        if visited[friend] == 1:
            continue
        num_friends = num_candies = 0
        dfs(friend)
        friends_set.append([num_candies, num_friends])

    dp = [[0] * K for _ in range(len(friends_set))]
    for idx, f_set in enumerate(friends_set):
        for people in range(1, K):
            
            # 현재 f_set의 인원 > people
            if f_set[1] > people:
                dp[idx][people] = dp[idx - 1][people]
            
            # # 현재 f_set의 인원 <= people
            else:
                dp[idx][people] = max(dp[idx - 1][people], dp[idx - 1][people - f_set[1]] + f_set[0])

    print(dp[-1][-1])