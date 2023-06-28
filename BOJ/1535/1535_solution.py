import sys
sys.stdin = open('1535_input.txt')

## 접근법 ##
# 1. input을 잃는 체력이 작은 순으로 정렬한다.
# 2. knapsack 함수를 정의한다.

def knapsack(h, w):
    # 현재 사람의 체력을 감당할 수 없을 때
    if data[h][0] > w:
        if h:
            memo[h][w] = memo[h-1][w]

    # 현재 사람의 체력을 감당할 수 있을 때
    else:
        # h가 1 이상인 경우
        if h:
            # 이전 h의 동일한 무게 vs (현재 h로부터 얻는 기쁨 + 이전 h에서 현재 h를 넣을 공간을 마련했을 때 기쁨)
            memo[h][w] = max(memo[h-1][w], data[h][1] + memo[h-1][w-data[h][0]])
        
        # h가 0인 경우
        else:
            memo[h][w] = data[h][1]

N = int(input())

health = list(map(int, sys.stdin.readline().split()))
joy = list(map(int, sys.stdin.readline().split()))

data = []
for i in range(N):
    data.append([health[i], joy[i]])

data.sort()

memo = [[0] * 100 for _ in range(N)]

for i in range(N):
    for j in range(100):
        knapsack(i, j)

print(memo[-1][-1])