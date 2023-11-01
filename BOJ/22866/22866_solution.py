import sys
sys.stdin = open('22866_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
buildings = list(map(int, input().split()))

# 우측 방향으로 자신보다 높은 빌딩의 인덱스 저장
forward = [i for i in range(N)]
forward[N -1] = N

# 좌측 방향으로 자신보다 높은 빌딩의 인덱스 저장
backward = [i for i in range(N)]
backward[0] = -1

# 각 빌딩에서 보이는 빌딩 개수: [왼쪽, 오른쪽]
visible = [[0, 0] for i in range(N)]

# 우측 방향으로 자신보다 높은 빌딩 찾아가기
def find_f(n, target):
    parent = forward[n]
    # 끝에 도달하면 자신보다 높은 빌딩 없음
    if parent == N:
        return -1
    elif buildings[parent] > target:
        return parent
    # 자신과 동일한 높이의 빌딩이 가장 높은 빌딩
    elif parent == n:
        return -1
    else:
        return find_f(parent, target)

# 좌측 방향으로 자신보다 높은 빌딩 찾아가기
def find_b(n, target):
    parent = backward[n]
    # 끝에 도달하면 자신보다 높은 빌딩 없음
    if parent == -1:
        return -1
    elif buildings[parent] > target:
        return parent
    # 자신과 동일한 높이의 빌딩이 가장 높은 빌딩
    elif parent == n:
        return -1
    else:
        return find_b(parent, target)

for i in range(1, N):
    idx_forward = N - i - 1
    idx_backward = i

    # 바로 왼쪽 빌딩이 현재 빌딩보다 높은 경우
    if buildings[idx_backward - 1] > buildings[idx_backward]:
        visible[idx_backward][0] = visible[idx_backward - 1][0] + 1
        backward[idx_backward] = idx_backward - 1
    else:
        parent = find_b(idx_backward - 1, buildings[idx_backward])
        
        # 더 높은 빌딩이 없을 경우
        if parent == -1:
            visible[idx_backward][0] = 0
        else:
            visible[idx_backward][0] += visible[parent][0] + 1
            backward[idx_backward] = parent

    
    # 바로 오른쪽 빌딩이 현재 빌딩보다 높은 경우
    if buildings[idx_forward + 1] > buildings[idx_forward]:
        visible[idx_forward][1] = visible[idx_forward + 1][1] + 1
        forward[idx_forward] = idx_forward + 1

    else:
        parent = find_f(idx_forward + 1, buildings[idx_forward])

        # 더 높은 빌딩이 없을 경우
        if parent == -1:
            visible[idx_forward][1] = 0
        else:
            visible[idx_forward][1] += visible[parent][1] + 1
            forward[idx_forward] = parent

for i in range(N):
    left = visible[i][0]
    left_dist = 100000

    right = visible[i][1]
    right_dist = 100000

    if left != 0:
        left_dist = i - backward[i]
    if right != 0:
        right_dist = forward[i] - i
    
    # 양방향으로 볼 수 있는 빌딩이 없을 경우
    if left == 0 and right == 0:
        print(0) 
        
    # 오른쪽으로만 볼 수 있는 빌딩이 있을 경우
    elif left_dist > right_dist:
        print(left + right, forward[i] + 1)
        
    # 왼쪽으로만 볼 수 있는 빌딩이 있을 경우
    else:
        print(left + right, backward[i] + 1)
