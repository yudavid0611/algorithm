import sys
from collections import Counter
sys.stdin = open('17299_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))

# 각 원소별 출현 빈도
cnt_nums = Counter(nums)

# 가장 많은 빈도
most_frequent = max(cnt_nums.values())

stack = []

# str(): 정답 출력시 join 메서드를 활용하기 위해
answer = [str(-1)] * N

for idx, n in enumerate(nums):
    # 스택이 비었을 경우
    if not stack:
        # n의 출현 빈도가 most_frequent일 경우
        if cnt_nums[n] == most_frequent:
            answer[idx] = str(-1)
        else:
            stack.append([n, idx])
    
    # 스택에 원소가 있을 때
    else:
        # stack의 마지막 원소 출현 빈도 >= n의 출현 빈도
        if cnt_nums[stack[-1][0]] >= cnt_nums[n]:
            stack.append([n, idx])
        else:
            # 스택에 원소가 있고, 마지막 원소의 출현 빈도가 n의 출현빈도보다 작을 때까지 pop
            while stack and cnt_nums[stack[-1][0]] < cnt_nums[n]:
                _, idx_element = stack.pop()
                answer[idx_element] = str(n)
            
            # n의 출현 빈도가 most_frequent일 경우
            if cnt_nums[n] == most_frequent:
                answer[idx] = str(-1)
            else:
                stack.append([n, idx])

print(' '.join(answer))