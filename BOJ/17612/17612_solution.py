import sys
import heapq
sys.stdin = open('17612_input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(N)]

counters = []
init_counter = min(N, K)

# 일단 계산대에 고객 모두 채우기
for i in range(init_counter):
    # heappush -> [물건 수, 계산대, id]
    heapq.heappush(counters, [customers[i][1], i, customers[i][0]])

# 계산이 끝난 고객 저장
customers_out = []
for customer in customers[init_counter:]:
    # 계산이 가장 빨리 끝나면서, 계산대 번호가 가장 작은 계산대 pop
    stuff_agg, counter, id_customer = heapq.heappop(counters)

    # popped 고객은 계산 완료
    customers_out.append([stuff_agg, counter, id_customer])

    # 현재 고객의 물건 수 추가
    stuff_agg += customer[1]
    heapq.heappush(counters, [stuff_agg, counter, customer[0]])

# counters에 남아 있는 고객들 처리
while counters:
    stuff_agg, counter, id_customer = heapq.heappop(counters)
    customers_out.append([stuff_agg, counter, id_customer])

# 기다린 시간 오름차순 -> 계산대 내림차순 정렬
sort_key = lambda x: (x[0], -x[1])
customers_out = sorted(customers_out, key=sort_key)

answer = 0
for idx, customer in enumerate(customers_out, 1):
    answer += idx * customer[2]

print(answer)