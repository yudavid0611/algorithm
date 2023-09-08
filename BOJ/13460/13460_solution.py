import sys
from collections import deque
sys.stdin = open('13460_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

# red와 blue의 위치를 저장
visited = set()

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)

# queue
q = deque()
q.append([red, blue, 0])

visited.add((red, blue))

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 먼저 움직여야 하는 구슬을 찾는 함수
def find_first_move(r, b, d):
    
    # 위로 움직이는 경우
    if d == [-1, 0]:
        if r[1] != b[1]:
            return -1
        
        # r과 b가 같은 열에 있을 경우
        else:
    
            # r이 b보다 위쪽에 있을 경우
            if r[0] < b[0]:
                return 'r'
            
            # b가 r보다 위쪽에 있을 경우
            else:
                return 'b'
            
    
    # 오른쪽으로 움직이는 경우
    elif d == [0, 1]:
        if r[0] != b[0]:
            return -1
        
        else:
            if r[1] < b[1]:
                return 'b'
            
            else:
                return 'r'
    
    # 아래로 움직이는 경우
    elif d == [1, 0]:
        if r[1] != b[1]:
            return -1
        
        else:
            if r[0] < b[0]:
                return 'b'
            
            else:
                return 'r'
    
    # 왼쪽으로 움직이는 경우
    else:
        if r[0] != b[0]:
            return -1
        
        else:
            if r[1] < b[1]:
                return 'r'
            
            else:
                return 'b'

# 구슬 x를 움직이는 함수
def move(x, y, d):
    '''
    x: 현재 움직이는 구슬
    y: 다른 구슬
    '''
    row, col = x

    # 움직일 수 있을 때까지 계속 움직임
    while True:
        new_row = row + d[0]
        new_col = col + d[1]

        if 0 <= new_row < N and 0 <= new_col < M and board[new_row][new_col] != '#' and (new_row, new_col) != y:
            row, col = new_row, new_col
            
            # 구멍에 들어간 경우
            if board[row][col] == 'O':
                return (-1, -1)
        else:
            break
    
    return (row, col)


# 판을 기울였을 때 작동하는 매커니즘 함수
def spin(r, b, d):

    # 어떤 구슬을 먼저 움직일지 확인
    first = find_first_move(r, b, d)

    # r을 먼저 움직일 경우
    if first == 'r':
        r = move(r, b, d)
        b = move(b, r, d)
    
    # b를 먼저 움직일 경우
    else:
        b = move(b, r, d)
        r = move(r, b, d)

    # r이 구멍에 들어간 경우    
    if r == (-1, -1):

        # 둘 다 구멍에 들어간 경우
        if b == (-1, -1):
            return 'impossible'
        
        # r만 구멍에 들어간 경우
        else:
            return 'goal'

    beads = (r, b)
    
    # 이미 도달했던 위치이거나, b만 구멍에 들어간 경우
    if beads in visited or b == (-1, -1):
        return 'impossible'
    
    else:
        # 위치 저장
        visited.add(beads)

    return (r, b)

# 결과 초기값
answer = 100
while q:
    r, b, count = q.popleft()

    # 10번 이상 움직여야 할 경우 다음 케이스로
    if count == 10:
        continue

    for d in delta:
        result = spin(r, b, d)

        # 해당 방향으로 움직일 수 없는 경우
        if result == 'impossible':
            continue
        
        # r이 구멍에 들어간 경우
        if result == 'goal':
            if count + 1 < answer:
                answer = count + 1
        
        else:
            q.append((result[0], result[1], count + 1))

if answer == 100:
    print(-1)

else:
    print(answer)