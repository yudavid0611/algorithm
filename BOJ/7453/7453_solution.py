import sys
from collections import defaultdict
sys.stdin = open('7453_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())

nums = [[], [], [], []]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    nums[0].append(a)
    nums[1].append(b)
    nums[2].append(c)
    nums[3].append(d)

# key: A와 B의 합, value: 해당 key의 개수
sum_ab = defaultdict(int)
for i in nums[0]:
    for j in nums[1]:
        sum_ab[i + j] += 1

answer = 0

for i in nums[2]:
    for j in nums[3]:
        target = -(i + j)
        # 0으로 만들 수 있는 수가 sum_ab에 있는지 확인
        if target in sum_ab:
            answer += sum_ab[target]

print(answer)