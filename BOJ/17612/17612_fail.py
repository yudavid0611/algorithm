# 시간 초과
import sys
import heapq
sys.stdin = open('17612_input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0
customers = []

# 정답 출력
def print_answer(customers):
    answer = 0
    
    # 기다린 시간 오름차순 -> 계산대 내림차순 정렬
    sort_key = lambda x: (x[0], -x[1])
    customers_sorted = sorted(customers, key=sort_key)
    
    for idx, customer in enumerate(customers_sorted, 1):
        answer += idx * customer[2]
    
    return answer


for _ in range(N):
    i, w = map(int, input().split())
    
    # [기다리는 시간, 계산대, id, 해당 고객의 물건 수]
    customers.append([0, 0, i, w])

counters = []
init_counter = min(N, K)

# 고객 수보다 계산대 수가 더 많으면 모든 고객 한 번에 처리 가능
if init_counter == N:
    for customer in enumerate(customers, 1):
        print(print_answer(customers))

else:
    # 일단 계산대에 고객 모두 채우기
    for i in range(init_counter):
        customers[i][0] = customers[i][3]
        customers[i][1] = i
        heapq.heappush(counters, [customers[i][3], i])

    for customer in customers[init_counter:]:
        # 계산이 가장 빨리 끝나면서, 계산대 번호가 가장 작은 계산대 pop
        time_agg, counter = heapq.heappop(counters)
        time_agg += customer[3]
        customer[0] = time_agg
        customer[1] = counter
        heapq.heappush(counters, [time_agg, counter])

    print(print_answer(customers))