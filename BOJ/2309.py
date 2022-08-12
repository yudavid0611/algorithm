# import sys
# sys.stdin = open('BOJ/input.txt', 'r')
height = []
for _ in range(9):
    height.append(int(input()))

# 키를 오름차순으로 정렬
height.sort()

# left 포인터와 right 포인터 생성
left = 0
right = len(height)-1

# 주어진 height의 총합 구하기
height_sum = sum(height)

while True:
    # 총합에서 left와 right에 해당하는 키를 뺐을 때 100이 되는 경우
    if height_sum - height[left] - height[right] == 100:
        break
    # 총합에서 left와 right에 해당하는 키를 뺐을 때 100보다 큰 경우
    elif height_sum - height[left] - height[right] > 100:
        left += 1
    # 총합에서 left와 right에 해당하는 키를 뺐을 때 100보다 작은 경우
    else:
        right -= 1

# lefe와 right에 해당하는 값 제외
del height[left]
# left에 해당하는 값이 빠졌기 때문에 right-1
del height[right-1]

for i in height:
    print(i)