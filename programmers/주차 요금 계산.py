import math
from collections import defaultdict

# 시간 계산 함수
# times = [입차 시간, 출차 시간]
def get_time(times):
    results = []
    for time in times:
        hours = int(time[:2]) * 60
        minutes = int(time[3:5])
        results.append(hours + minutes)
    return results[1] - results[0]


# 비용 계산 함수
def get_cost(time, fees):
    # 기본 시간을 초과하지 않은 경우
    if time <= fees[0]:
        return fees[1]
    
    # 기본 시간을 초과한 경우
    else:
        over_time = time - fees[0]
        # 올림 처리
        over_time = math.ceil(over_time / fees[2])
        result = int(fees[1] + over_time * fees[3])
        return result
    
def solution(fees, records):
    cars = defaultdict(list)
    
    for record in records:
        time, car, _ = record.split()
        
        # 처음 처리하는 차량인 경우
        if not cars[car]:
            cars[car] = [0, time]
        else:
            # 입차 처리
            if not cars[car][1]:
                cars[car][1] = time
            
            # 출차 처리
            else:
                parked_time = get_time([cars[car][1], time])
                cars[car][0] += parked_time
                cars[car][1] = 0
    
    for car in cars.items():
        # 출차하지 않은 경우
        if car[1][1]:
            parked_time = get_time([car[1][1], '23:59'])
            cars[car[0]][0] += parked_time
            cars[car[0]][1] = 0
    
        # 비용 계산
        cost = get_cost(car[1][0], fees)
        car[1][0] = cost
    
    # 차 번호 오름차순으로 정렬
    temp = sorted(cars.items())
    
    # 주차요금만 추출하기
    f = lambda x:x[1][0]
    answer = list(map(f, temp))

    return answer