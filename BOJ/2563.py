# import sys
# sys.stdin = open('BOJ/input.txt', 'r')

box_num = int(input())
boxes = []

# 각 색종이의 벽으로부터의 거리를 담은 리스트를 boxes에 append
for i in range(box_num):
    boxes.append(list(map(int, input().split())))

# 검은 영역을 나타낼 변수 생성
black = 0

# 도화지를 넓이가 1인 칸으로 나누고 각 칸의 좌표를 (x, y)의 형태로 가정
# 0 <= x, y <= 99
for x in range(100):
    for y in range(100):
        for b in boxes:
            # 색종이의 왼쪽 벽으로부터의 거리와 아래쪽 벽으로부터의 거리가 조건에 맞을 경우 black += 1
            if (x-9<=b[0]<=x) and (y-9<=b[1]<=y):
                black += 1
                # 같은 칸이 중복으로 카운트되지 않도록 break
                break
print(black)