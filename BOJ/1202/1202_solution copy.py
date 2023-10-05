import sys
import heapq
sys.stdin = open('1202_input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

jewel = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input().rstrip()) for _ in range(K)]

jewel = sorted(jewel)
bags = sorted(bags)

price = 0
j_idx = 0
jewel_in_bags = []

for bag in bags:
    
    # 현재 가방에 넣을 수 있는 보석을 모두 저장
    while j_idx < N and bag >= jewel[j_idx][0]:
        heapq.heappush(jewel_in_bags, -jewel[j_idx][1])
        j_idx += 1
    
    # 현재 가방들에 들어 있는 보석 중 가장 가치가 큰 보석값 더하기
    if jewel_in_bags:
        price -= heapq.heappop(jewel_in_bags)

print(price)