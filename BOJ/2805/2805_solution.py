import sys
sys.stdin = open('2805_input.txt')

## 접근법 ##
# 1. 0과 가장 길이가 긴 나무의 길이를 양 끝점으로 이진 탐색 수행
# 2. 중간 지점에서 가져갈 수 있는 나무 길이가 M보다 크면 오른쪽 끝점을 중간지점으로 이동
# 3. 중간 지점에서 가져갈 수 있는 나무 길이가 M보다 작으면 왼쪽 끝점을 중간지점으로 이동
# M을 정확히 얻을 수 있으면 해당 지점이 정답
# M을 정확히 얻지 못하면, 두 끝점이 만난 지점 +1이 정답

N, M = map(int, input().split())

trees = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
trees.sort()

# 왼쪽, 오른쪽 포인터
left = 0
right = trees[-1]
while left <= right:
    middle = (left + right) // 2

    # 나무를 자르고 가져갈 수 있는 양
    cut = 0
    for tree in trees[::-1]:
        if tree <= middle:
            break

        cut += tree - middle
    
    # 정확히 M만큼 가져갈 수 있을 경우 break
    if cut == M:
        break
    # 가져갈 수 있는 양을 줄이도록 left 포인터 옮기기
    elif cut > M:
        left = middle + 1
    # 가져갈 수 있는 양을 늘리도록 right 포인터 옮기기
    else:
        right = middle - 1

if left > right:
    print(right)
else:
    print(middle)