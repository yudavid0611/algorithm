import sys
from collections import deque

## 테스트케이스 약 10% 정도까지 통과 후 시간초과 ##

sys.stdin = open('2981_input.txt')

N = int(input())

nums = deque()
for _ in range(N):
    nums.append(int(input()))

nums = sorted(nums)

results = deque()

for i in range(2, nums[1]):
    remainder = nums[0] % i

    for n in nums[1:]:
        if n % i != remainder:
            break
    else:
        results.append(i)
results = list(map(str, results))
results = ' '.join(sorted(results))
print(results)