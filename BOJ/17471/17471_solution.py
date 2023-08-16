import sys
from collections import defaultdict, deque
from itertools import combinations

sys.stdin = open('17471_input.txt')
input = sys.stdin.readline

N = int(input())

# 구역별 인구수
populations = [0] + list(map(int, input().split()))

# 인접 리스트
sections = defaultdict(list)

for section in range(1, N + 1):
    _, *adjs = map(int, input().split())
    sections[section] = adjs

# 선거구의 각 구역이 모두 연결되어 있는지 확인할 bfs 함수
def bfs(group, sections, populations):
    q = deque()
    visited = [0] * (N + 1)
    sum_population = 0

    start = group[0]
    q.append(start)
    visited[start] = 1
    sum_population += populations[start]

    while q:
        v = q.popleft()

        for next_v in sections[v]:
            # 아직 방문하지 않았고, 선거구 내 구역일 경우
            if visited[next_v] == 0 and next_v in group:
                visited[next_v] = 1
                sum_population += populations[next_v]
                q.append(next_v)

    if len(group) == sum(visited):
        return True, sum_population
    else:
        return False, sum_population

sections_number = sections.keys()

# 출력값 초기화
answer = 99 * N

for i in range(1, N // 2 + 1):
    # i개를 뽑는 조합 구하기
    groups = list(combinations(sections_number, i))
    
    for idx, group_a in enumerate(groups):
        group_a_is_possible, group_a_sum_population = bfs(group_a, sections, populations)

        # a선거구에 포함되지 않은 구역들 추출하기
        group_b = tuple(filter(lambda x: x not in group_a, sections_number))
        group_b_is_possible, group_b_sum_population = bfs(group_b, sections, populations)

        # 두 선거구의 구역들 모두 인접 관계일 경우
        if group_a_is_possible and group_b_is_possible:
            diff = abs(group_a_sum_population - group_b_sum_population)

            if diff < answer:
                answer = diff

# 선거구를 나눌 수 없는 경우 -1 출력
if answer == 99 * N:
    print(-1)
else:
    print(answer)