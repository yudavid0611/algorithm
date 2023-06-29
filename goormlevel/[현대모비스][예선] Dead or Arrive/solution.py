import sys
from collections import defaultdict

sys.stdin = open('input.txt')

n = int(input())

results = defaultdict(list)

for i in range(1, n + 1):
	v, w = map(int, sys.stdin.readline().split())
	
	# 해당 속도에 등록된 차량이 없을 경우
	if not results[v]:
		results[v] = [w, i]
		
	# 해당 속도에 등록된 차량이 있을 경우
	else:
		# 내구도 체크
		if w >= results[v][0]:
			results[v] = [w, i]

f = lambda x: x[1]
cars = list(results.values())
cars = list(map(f, cars))
print(sum(cars))
