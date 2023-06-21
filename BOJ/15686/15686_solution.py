import sys
from itertools import combinations 
sys.stdin = open('15686_input.txt')

## 접근법 ##
# 1. 치킨집 조합을 구한다.
# 2. 집을 순회하며 각 집의 치킨 거리를 구한다.
# 3. 도시의 치킨 거리를 구하는 과정에서 기존 최소 거리를 초과하면 
#   다음 치킨집 조합으로 넘어간다.

# 각 집의 치킨 거리 계산 함수
def get_dist(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

N, M = map(int, input().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = N ** 3

chicken_all = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken_all.append([i, j])

chicken_comb = combinations(chicken_all, M)

for chicken in chicken_comb:
    temp_result = 0

    for h in house:
        min_dist = N ** 2
        
        for c in chicken:
            dist = get_dist(h, c)
            if dist < min_dist:
                min_dist = dist
        
        temp_result += min_dist
        if temp_result >= result:
            break
    
    if temp_result < result:
        result = temp_result

print(result)