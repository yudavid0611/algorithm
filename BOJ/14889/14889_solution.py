import sys
from itertools import combinations
sys.stdin = open('BOJ/14889/14889_input.txt', 'r')


def comb(arr):
    global teams
    half = list(combinations(arr, N//2))                            # N의 절반만큼의 원소 수를 가지는 모든 조합 구하기
    for h in half:
        temp = arr[:]
        for i in h:
            temp.remove(i)                                          # 조합에 포함되지 않은 원소 집합
        teams.append((tuple(h), tuple(temp)))
        teams = tuple(map(sorted, teams))                               # 리스트 내 첫 번째 원소는 스타트팀, 두 번째 원소는 링크팀
        teams = tuple(map(tuple, teams))                               # 리스트 내 첫 번째 원소는 스타트팀, 두 번째 원소는 링크팀
        teams = list(set(teams))


def get_score(arr):                                                 # 능력치를 계산하는 함수
    result = 0
    for (i, j) in arr:
        result += scores[i-1][j-1] + scores[j-1][i-1]               # scores와 인덱스를 맞추기 위해 i와 j에 -1
    return result


N = int(input())                                                    # 선수의 수

scores = [list(map(int, input().split())) for _ in range(N)]        # 능력치 2차원 리스트
players = [i for i in range(1, N+1)]                                # 선수들의 번호 생성
teams = []                                                          # 팀 배정 경우의 수를 저장할 리스트
comb(players)       
min_value = 200 * len(list(combinations(players[:N//2], 2)))        # 능력치 차의 최소값 초기화
for t in teams:
    a_possible = list(combinations(t[0], 2))                        # 스타트팀의 가능한 능력치 순서쌍 구하기
    b_possible = list(combinations(t[1], 2))                        # 링크팀의 가능한 능력치 순서쌍 구하기
    temp_min = get_score(a_possible)
    temp_min = abs(temp_min - get_score(b_possible))
    if temp_min < min_value:                                        # 최소값 갱신
        min_value = temp_min
print(min_value)