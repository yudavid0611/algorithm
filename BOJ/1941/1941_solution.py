import sys
from itertools import combinations
from collections import defaultdict
sys.stdin = open('1941_input.txt')
input = sys.stdin.readline

seats = [input().rstrip() for _ in range(5)]

coordinate = [[i, j] for i in range(5) for j in range(5)]

# 25개 자리 중 7개를 뽑는 조합 구하기
combs = combinations(coordinate, 7)

# 상, 우, 하, 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# dfs를 통해 인접 여부 확인
def check_adj(comb, delta=delta):
    stack = []
    visited = defaultdict(int)
    
    r, c = comb[0]
    visited[(r, c)] = 1

    while True:
        for d in delta:
            new_r = r + d[0]
            new_c = c + d[1]
            
            if 0 <= new_r < 5 and 0 <= new_c < 5 and [new_r, new_c] in comb and visited[(new_r, new_c)] == 0:
                stack.append([r, c])
                visited[(new_r, new_c)] = 1
                r, c = new_r, new_c
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break

    sum_values = sum(visited.values())
    if sum_values == len(comb):
        return True
    else:
        return False


# 인원 구성 확인
def check_people(comb, seats):
    n_S = 0
    
    for i,j in comb:
        if seats[i][j] == 'S':
            n_S += 1
    
    if n_S >= 4:
        return True
    else:
        return False


answer = 0
for comb in combs:
    
    # 인접 여부 확인
    is_adj = check_adj(comb)
    if not is_adj:
        continue

    # 인원 구성 확인
    pepole_valid = check_people(comb, seats)
    if pepole_valid:
        answer += 1
        
print(answer)

