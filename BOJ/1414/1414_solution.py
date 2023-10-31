import sys
import heapq
sys.stdin = open('1414_input.txt')
input = sys.stdin.readline

# 문자열을 숫자로 변환(아스키코드 사용)
def char_to_num(c):
    # 0일 경우
    if c == '0':
        return 0
    
    # 소문자일 경우
    elif c.islower():
        return ord(c) - 96
    
    # 대문자일 경우
    else:
        return ord(c) - 38

# 최소신장트리(프림 알고리즘)
def mst(v):
    global total_cable

    # 방문 표시
    visited = [0] * N

    # 인자로 받은 정점 방문 표시
    visited[v] = 1
    count_visited = 1

    # 사용한 케이블의 길이 저장
    used_cable = 0

    # 간선 후보
    cand = []
    while count_visited < N:
        for i in range(N):
            if visited[i] == 1:
                continue
            if computers[v][i] != 0:
                heapq.heappush(cand, [computers[v][i], i])
            if computers[i][v] != 0:
                heapq.heappush(cand, [computers[i][v], i])

        while cand:
            w, next_v = heapq.heappop(cand)
            if visited[next_v] == 0:
                break
        
        # cand가 없을 경우 더 이상 이동 불가
        else:
            used_cable = total_cable + 1
            break
        
        # 더 이상 이동할 수 있는 정점 없는 경우
        if visited[next_v] == 1:
            used_cable = total_cable + 1
            break

        used_cable += w
        v = next_v
        visited[v] = 1
        count_visited += 1

    return used_cable

if __name__ == '__main__':
    N = int(input().rstrip())
    computers = []
    total_cable = 0
    for _ in range(N):
        row = input().rstrip()
        new_row = []
        for r in row:
            new_row.append(char_to_num(r))
        total_cable += sum(new_row)
        computers.append(new_row)

    print(total_cable - mst(0))